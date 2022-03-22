let x = 0;
function speedTest1() {
    let keys = 39;
    if (keys == 39) {
        x = x + 1;
    }
    else if (keys == 37) {
        x = x - 1;
    }
    else if (keys == 38) {
        x = x - 1;
    }
    else if (keys == 40) {
        x = x - 1;
    }
    else if (keys == 41) {
        x = x - 1;
    }
    else if (keys == 42) {
        x = x - 1;
    }
    else if (keys == 43) {
        x = x - 1;
    }
    else if (keys == 44) {
        x = x - 1;
    }
}

let iterations = 2500000000;
console.time('Function #2');
for (let i = 0; i < iterations; i++) {
    speedTest1();
};
console.timeEnd('Function #2');
