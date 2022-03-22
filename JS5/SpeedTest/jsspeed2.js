let x = 0;
function speedTest1() {
    let keys = 39;
    if (keys == 39) {
        x = x + 1;
    }
    else if (keys == 37) {
        x = x - 1;
    }
}

let iterations = 5000000000;
console.time('Function #1');
for (let i = 0; i < iterations; i++) {
    speedTest1();
};
console.timeEnd('Function #1');
