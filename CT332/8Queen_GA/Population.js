class Population {
  constructor(m, num) {
    this.generations = 0; // Number of generations
    this.finished = false; // Are we finished evolving?
    this.mutationRate = m; // Mutation rate
    this.maxFitness = 28;

    this.best = "";
    this.bestCoord = [];

    this.population = [];
    for (let i = 0; i < num; i++) this.population[i] = new Chromosome();

    this.probability = [];
  }

  // Fill our fitness array with a value for every member of the population
  calcFitness() {
    for (let i = 0; i < this.population.length; i++)
      this.population[i].calcFitness();
  }

  randomSelection() {
    let n = floor(this.population.length * 0.5);
    let r = floor(random(n));
    return this.population[r];
  }

  // randomSelection() {
  //   let r = random(1);
  //   let i = 0;
  //   while (r > 0) {
  //     r -= this.probability[i];
  //     i++;
  //   }
  //   i--;
  //   return this.population[i];
  // }

  // Create a new generation
  generate() {
    for (let i = 0; i < this.population.length - 1; i++)
      for (let j = i + 1; j < this.population.length; j++)
        if (this.population[i].fitness < this.population[j].fitness) {
          let temp = this.population[i];
          this.population[i] = this.population[j];
          this.population[j] = temp;
        }

    let sum = 0;
    for (let i = 0; i < this.population.length; i++)
      sum += this.population[i].fitness;
    for (let i = 0; i < this.population.length; i++)
      this.probability[i] = this.population[i].fitness / sum;

    let newPopulation = [];
    for (let i = 0; i < this.population.length; i++) {
      let partnerA = this.randomSelection();
      let partnerB = this.randomSelection();
      let child = partnerA.crossover(partnerB);
      child.mutate(this.mutationRate);
      newPopulation[i] = child;
    }

    this.population = newPopulation;
    this.generations++;
  }

  getBest() {
    return this.best;
  }

  getBestCoord() {
    return this.bestCoord;
  }

  // Compute the current "most fit" member of the population
  evaluate() {
    let maxFit = 0;
    let index = 0;
    for (let i = 0; i < this.population.length; i++)
      if (this.population[i].fitness > maxFit) {
        index = i;
        maxFit = this.population[i].fitness;
      }

    this.best = this.population[index].getState();
    this.bestCoord = this.population[index].getCoord();

    if (maxFit == this.maxFitness || this.generations >= 2000)
      this.finished = true;
  }

  isFinished() {
    return this.finished;
  }

  getGenerations() {
    return this.generations;
  }

  getAverageFitness() {
    let total = 0;
    for (let i = 0; i < this.population.length; i++)
      total += this.population[i].fitness;
    return total / this.population.length;
  }

  getMaxFitness() {
    let maxFitness = 0;
    for (let i = 0; i < this.population.length; i++)
      if (this.population[i].fitness > maxFitness)
        maxFitness = this.population[i].fitness;
    return maxFitness;
  }

  allStates() {
    let everything = "";

    let displayLimit = min(this.population.length, 100);

    for (let i = 0; i < displayLimit; i++)
      everything +=
        this.population[i].getState() +
        " | " +
        this.population[i].fitness +
        "<br>";

    return everything;
  }
}
