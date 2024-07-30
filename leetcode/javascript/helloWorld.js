/**
 * Function Syntax with Rest
 */
var createHelloWorld = function() {
    
    return function() {
        return "Hello World";
    }
};

/**
* Arrow Syntax
var createHelloWorld = function() {
    
    return () => "Hello World";
};
 */

/**
*Rest and Arrow Syntax
var createHelloWorld = function() {
    
    return (...args) => "Hello World";
};
 */

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
