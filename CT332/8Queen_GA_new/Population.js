class Population {
  constructor(m, num) {
    this.generations = 0;
    this.finished = false;
    this.mutationRate = m;
    this.maxFitness = 28;

    this.best = "";
    this.bestCoord = [];

    this.population = [];
    for (let i = 0; i < num; i++)
      this.population[i] = new Chromosome();
    
    this.probability = [];
  }

  calcFitness() {
    for (let i = 0; i < this.population.length; i++)
      this.population[i].calcFitness();
  }

  randomSelection() {
    let r = random(1);
    let i = 0;
    while (r > 0){
      r -= this.probability[i];
      i++;
    }
    i--;
    return this.population[i];
  }

  generate() {
    let sum = 0;
    for (let i = 0; i < this.population.length; i++) 
      sum += this.population[i].fitness;
    for (let i = 0; i < this.population.length; i++) 
      this.probability[i] = this.population[i].fitness / sum;
    
    for (let i = 0;i < this.population.length - 1;i++)
      for (let j = i + 1;j < this.population.length;j++)
        if (this.population[i].probability < this.population[j].probability){
          let temp = this.population[i];
          this.population[i] = this.population[j];
          this.population[j] = temp;
        }

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

  evaluate() {
    let maxFit = 0;
    let index = 0;
    for (let i = 0; i < this.population.length; i++)
      if (this.population[i].fitness > maxFit) {
        index = i;
        maxFit = this.population[i].fitness;
      }

    this.best = this.population[index].getGenes();
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

  getMaxFitness(){
    let maxFitness = 0;
    for (let i = 0; i < this.population.length; i++) 
      if (this.population[i].fitness > maxFitness)
        maxFitness = this.population[i].fitness;
    return maxFitness;
  }

  allChromosomes() {
    let everything = "";

    let displayLimit = min(this.population.length, 100);

    for (let i = 0; i < displayLimit; i++) 
      everything += this.population[i].getGenes() + " | " + this.population[i].fitness + "<br>";
    
    return everything;
  }
}