function getSkills() {
    fetch("https://zany-skitter-caper.glitch.me/skills").then(_Response => {
        if (_Response.ok) {
            console.log("Duomenys gauti");
            return _Response.json();
        } else {
            console.log("Kažkas negerai");
        }
    }).then(_APIData => {
        document.getElementById("profile_skills").innerHTML = "";
        console.log(_APIData);
        CreateSkills(_APIData);
    }).catch(err => console.log("nepavyko", err))
}

function CreateSkills(AData) {
    AData.forEach((AItem, AIndex) => {
        CreateSkill(AItem);
    });
}

function CreateSkill(AItem) {
    let _SingleSkill = document.createElement('div');
    _SingleSkill.setAttribute('class', 'single_skill');

    let _SkillDiv = document.createElement('div');
    _SkillDiv.setAttribute('class', 'skill_div');
    _SingleSkill.appendChild(_SkillDiv);

    let _SkillName = document.createElement('p');
    _SkillName.innerText = AItem.title;
    _SkillName.setAttribute('class', 'skill_name');
    _SkillDiv.appendChild(_SkillName);

    let _SkillPercent = document.createElement('p');
    _SkillPercent.innerText = AItem.level + "%";
    _SkillPercent.setAttribute('class', 'skill_percent');
    _SkillDiv.appendChild(_SkillPercent);

    let _SkillProgress = document.createElement('progress');
    _SkillProgress.value = parseInt(AItem.level);
    let _ProgressID = AItem.title + AItem.level;
    console.log(_ProgressID);
    _SkillProgress.id = _ProgressID;
    _SkillProgress.max = 100;
    _SingleSkill.appendChild(_SkillProgress);

    document.getElementById('profile_skills').appendChild(_SingleSkill);
}

getSkills();