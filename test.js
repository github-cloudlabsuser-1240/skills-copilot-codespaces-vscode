class Calculator {
    add(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }

    multiply(a, b) {
        return a * b;
    }

    divide(a, b) {
        if (b === 0) {
            throw new Error("Division by zero is not allowed.");
        }
        return a / b;
    }
}

function main() {
    const calculator = new Calculator();
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Welcome to the Calculator!");
    console.log("Options:");
    console.log("1. Add");
    console.log("2. Subtract");
    console.log("3. Multiply");
    console.log("4. Divide");
    console.log("5. Quit");

    readline.question("Enter your choice (1/2/3/4/5): ", (choice) => {
        if (choice === '5') {
            console.log("Thanks for using the calculator. Goodbye!");
            readline.close();
            return;
        }

        readline.question("Enter the first number: ", (num1) => {
            readline.question("Enter the second number: ", (num2) => {
                const a = parseFloat(num1);
                const b = parseFloat(num2);
                let result;

                try {
                    switch (choice) {
                        case '1':
                            result = calculator.add(a, b);
                            console.log(`Result: ${a} + ${b} = ${result}`);
                            break;
                        case '2':
                            result = calculator.subtract(a, b);
                            console.log(`Result: ${a} - ${b} = ${result}`);
                            break;
                        case '3':
                            result = calculator.multiply(a, b);
                            console.log(`Result: ${a} * ${b} = ${result}`);
                            break;
                        case '4':
                            result = calculator.divide(a, b);
                            console.log(`Result: ${a} / ${b} = ${result}`);
                            break;
                        default:
                            console.log("Invalid choice. Please restart the program and try again.");
                            break;
                    }
                } catch (error) {
                    console.log(error.message);
                }

                readline.close();
            });
        });
    });
}

main();