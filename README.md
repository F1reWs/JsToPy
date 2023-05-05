# JsToPy
A library that add to python some js functions.

## Installation
`pip3 install JsToPy` or `pip3 install --user JsToPy`

## Why JsToPy?
JsToPy makes JavaScript code using in Python.

JS code:
```js
var this = require("a-lib");

var nums = [];
nums.length = 10;
nums.fill("Foobar");
console.log(nums);
```

Using JsToPy:
```py
import JsToPy

this = require("a-lib");

nums = [];
nums.number = 10;
nums.fill("js in python");
console.log(nums);
```