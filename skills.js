// function to convert celsius to Fahrenheit
function celsiusToFahrenheit(celsius) {
    return celsius * 9/5 + 32;
}
// Driver code
let celsius = 37;
let fahrenheit = celsiusToFahrenheit(celsius);
console.log(`${celsius} degree celsius is equal to ${fahrenheit} degree fahrenheit.`);