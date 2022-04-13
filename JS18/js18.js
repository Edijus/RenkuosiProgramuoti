// 1
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    compareAge(other) {
        if (other > this.age) {
            console.log(this.name + " Petras is old enough to drink");
        } else {
            console.log(this.name + " Petras is old enough to drink milk");
        }
    }
}

const p1 = new Person("Petras", 16);
p1.compareAge(15);

// 2
function isNumber(char) {
    if (typeof char !== 'string') {
        return true;
    }

    if (char.trim() === '') {
        return false;
    }

    return !isNaN(char);
}

function ReturnNumbers(AArr) {
    let _NumberArray = [];
    let _text = "";
    for (let i = 0; i < AArr.length; i++) {
        _text = AArr[i];
        console.log(_text + " " + isNumber(_text));
        if (isNumber(_text)) {
            _NumberArray.push(_text);
        }
    }

    return _NumberArray;
}

console.log(ReturnNumbers([1, 5, "a", "g", "z", 6]));

// 3
function isAlpha(str) {
    return /^[a-zA-Z]+$/.test(str);
}

function DoubleChar(AText) {
    let result = "";
    for (let i = 0; i < AText.length; i++) {
        if (isAlpha(AText[i])) {
          result = result + AText[i] + AText[i];
        }else{
            result = result + AText[i];
        }
    }
    return result;
}

console.log(DoubleChar("Petras 123 Slekys_"));

// 4
function IsPostCodeValid(APostCode){
    let _NumberCount = 0;
    let _AlphaCount = 0;
    for(let i = 0; i < APostCode.length; i++){
        if(isNumber(APostCode[i])){
            _NumberCount++;
        }else if(isAlpha(APostCode[i])){
            _AlphaCount++;
        }
    }

    return ((APostCode.length == 5) && (_NumberCount == 5)) || ((_NumberCount == 3) && (_AlphaCount == 2));
}

console.log(IsPostCodeValid("123ab"));

// 5
function jazzify(AArr){
  let _NumberArray = [];
  let _LastChar = "";
  for(let i = 0; i < AArr.length; i++){
    _LastChar = AArr[i];
    _LastChar = _LastChar[_LastChar.length - 1];
    if(_LastChar == "7"){
        _NumberArray.push(AArr[i]);
    }else{
        _NumberArray.push(AArr[i] + "7");
    }
  }

  return _NumberArray;
}

console.log(jazzify(["FO", "E7", "A7", "Ab7", "Gm7", "C7"]));
