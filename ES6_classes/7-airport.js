export default class Airport {
    constructor(name, code) {
        this._name = name;
        this._code = code;
    }
    [Symbol.toStringTag](hint){
        return this._code;
    }
}