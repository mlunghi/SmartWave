# smartWave

### Inspiration
One of our team members was in Amsterdam when his friend asked him to make her a cheese quesadilla. He went for a shower and the quesadilla caught fire. To make sure something like this never happens again to anyone, our team came up with SmartWave - an intelligent microwave oven capable of monitoring their food as it gets heated up.

### What it does
The SmartWave uses computer vision technology to identify what food is inside it. As the food is gradually heated up, the built-in camera continues to monitor the shade changes of the food by taking recurring photos. Once the SmartWave has identified that the food has been cooked to perfection, it will automatically stop heating the food and notify the user that the food is ready to eat.

### How we built it
The prototype of SmartWave we created serves as a proof of concept. While we don't have an actual microwave, we built a model microwave oven for demoing purposes. The main result of our work is in the computer vision technology, supported by a Raspberry Pi computer, pi-camera, Javascript, PHP, and Python.

### Challenges we ran into
The most difficult challenge we ran into in this project was integrating all of the individual modules together. In order to combine the google cloud vision, Raspberry Pi, pi-camera, and other components of this project, we had to be very creative in our approach to the product. We also had to critically test how the functionalities of each component would interact with each other.

### Accomplishments that we're proud of
In spite of running into many challenges in the building process, we are proud of the final product we have delivered.

### What we learned
With google cloud vision's new updates, we are very proud that we were able to take full advantage of the program's capability to analyze image properties. We used this feature in order to identify the different color shades of food. This was essential for SmartWave to ensure that the food would be neither undercooked nor burnt.

### What's next for SmartWave
In the future we would like to create a fully functional microwave that uses the core technology we created at MakeHarvard to set its own cooking time. Furthermore, we would like to incorporate a more powerful computer so that we can obtain live footage inside the SmartWave rather than recurring snapshots. This way, we can improve the precision of the cooking time.

