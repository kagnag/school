class Chromosome {
  constructor() {
    this.genes = [];
    this.fitness = 0;
    for (let i = 0; i < 8; i++)
      this.genes[i] = floor(random(1, 9));
  }

  getGenes() {
    let s = "";
    let i;
    for (i = 0;i < this.genes.length - 1;i++){
      let c = str(this.genes[i]);
      s += c + ',';
    }
    let c = str(this.genes[i]);
    s += c;
    return s;
  }

  getCoord() {
    let q = [];
    for (let i = 0;i < this.genes.length;i++)
      q.push(this.genes[i]);
    return q;
  }

  calcFitness() {
    let count = 0;
    for (let i = 0; i < this.genes.length - 1; i++) {
      for (let j = i+1;j < this.genes.length;j++){
        if (this.genes[i] == this.genes[j]){
          count++;
        }
        else {
          if (abs(this.genes[i] - this.genes[j]) == j - i)
            count++;
        }
      }
    }
    this.fitness = 28 - count;
  }

  crossover(partner) {
    let child = new Chromosome();

    let midpoint = floor(random(this.genes.length));

    for (let i = 0; i < this.genes.length; i++) {
      if (i > midpoint) 
        child.genes[i] = this.genes[i];
      else 
        child.genes[i] = partner.genes[i];
    }
    return child;
  }

  mutate(mutationRate) {
    for (let i = 0; i < this.genes.length; i++)
      if (random(1) < mutationRate)
        this.genes[i] = floor(random(1, 9));
  }
}