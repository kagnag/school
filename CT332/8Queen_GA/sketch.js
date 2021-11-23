let popmax;
let mutationRate;
let population;

let bestState;
let allStates;
let stats;

let chessBoard;
let Queen = [];
let canvas;

function preload() {
  chessBoard = loadImage("chessBoard.png");
  for (let i = 0; i < 8; i++) Queen[i] = loadImage("Queen.png");
}

function setup() {
  popmax = 500;
  mutationRate = 0.01;

  population = new Population(mutationRate, popmax);

  canvas = createCanvas(440, 440);
  canvas.position(0, 80);

  bestState = createP("Best state:");
  bestState.position(10, -40);
  bestState.class("best");

  allStates = createP("All states:");
  allStates.position(600, 10);
  allStates.class("all");

  stats = createP("Stats");
  stats.position(10, 560);
  stats.class("stats");
}

function draw() {
  population.generate();

  population.calcFitness();

  population.evaluate();

  if (population.isFinished()) noLoop();

  displayInfo();

  // frameRate(1000);
}

function displayInfo() {
  bestState.html(
    "Best state:<br><br><br><br><br><br><br><br><br><br>" + population.getBest()
  );

  let statstext =
    "<br>total generations:     " + population.getGenerations() + "<br>";
  statstext +=
    "average fitness:       " + population.getAverageFitness() + "<br>";
  statstext += "max fitness:       " + population.getMaxFitness() + "<br>";
  statstext += "total population:      " + popmax + "<br>";
  statstext += "mutation rate:         " + floor(mutationRate * 100) + "%";

  stats.html(statstext);

  allStates.html("All states:<br>" + population.allStates());

  image(chessBoard, 0, 0, width, height);
  noFill();
  rect(0, 0, width, height);

  let bestCoord = population.getBestCoord();
  let w = floor(width / 8);
  let h = floor(height / 8);
  for (let i = 0; i < 8; i++) {
    let x = i * w;
    let y = (8 - bestCoord[i]) * h;
    image(Queen[i], x, y, w, h);
  }
}
