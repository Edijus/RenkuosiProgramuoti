const Automobiliai = [
    {
        "Marke": "Subaru",
        "Modelis": ["Impreza", "Forester"],
        "Pavarų_dežė": ["Mechaninė", "Automatinė"],
        "Kuro_tipas": ["Bezinas", "Dyzelis", "Dujos"],
        "Kebulo_tipas": "Universalas",
        "Kaina": 2000,
        "Stovis": ["Nauja", "Sena"],
    },

    {
        "Marke": "Fiat",
        "Modelis": ["500", "Brava"],
        "Pavarų_dežė": ["Mechaninė", "Automatinė"],
        "Kuro_tipas": ["Bezinas", "Dyzelis", "Dujos"],
        "Kebulo_tipas": "Kabrioletas",
        "Kaina": 3000,
        "Stovis": ["Nauja", "Sena"],
    },
    {
        "Marke": "Ford",
        "Modelis": ["Focus", "Mondeo"],
        "Pavarų_dežė": ["Mechaninė", "Automatinė"],
        "Kuro_tipas": ["Bezinas", "Dyzelis", "Dujos"],
        "Kebulo_tipas": "Enadas",
        "Kaina": 1000,
        "Stovis": ["Nauja", "Sena"],
    }
];

class TCar{
    constructor(AInfo){
      this.Make = AInfo.Marke;
      this.Model = AInfo.Modelis;
    }
};

let _Car = new TCar(Automobiliai[0]);
console.log(_Car.Make + " " + _Car.Model);