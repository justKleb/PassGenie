function genRandomSyms(leng) {
  if (typeof leng !== "number") {
    try {
      leng = parseInt(leng);
    } catch (error) {
      return "wrongType";
    }
  }
  let toConv = [];
  let base64Conv = "";
  for (let i = 0; i < leng; i++) {
    toConv.push(Math.floor(Math.random() * 10));
    if (toConv.length === leng) {
      let convStr = toConv.join("");
      base64Conv = btoa(convStr);
    }
    if (base64Conv.length > leng) {
      base64Conv = base64Conv.slice(0, leng - base64Conv.length);
    }
  }
  return base64Conv;
}

function mirror(toMirror) {
  if (typeof toMirror !== "string") {
    return "wrongType";
  }
  return toMirror.split("").reverse().join("");
}

function genRandomNums(leng) {
  if (typeof leng !== "number") {
    try {
      leng = parseInt(leng);
    } catch (error) {
      return "wrongType";
    }
  }
  let nums = [];
  for (let i = 0; i < leng; i++) {
    nums.push(Math.floor(Math.random() * 10));
  }
  return nums.join("");
}

function genRandomLetters(leng) {
  if (typeof leng !== "number") {
    try {
      leng = parseInt(leng);
    } catch (error) {
      return "wrongType";
    }
  }
  let lets = [];
  let letsBase = "abcdefghijklmnopqrstuvwxyz".split("");
  for (let i = 0; i < leng; i++) {
    lets.push(letsBase[Math.floor(Math.random() * 26)]);
  }
  return lets.join("");
}

async function genRandomWords(leng) {
  if (typeof leng !== "number") {
    try {
      leng = parseInt(leng);
    } catch (error) {
      return "wrongType";
    }
  }
  let wlist;
  try {
    const response = await fetch(
      "https://raw.githubusercontent.com/justKleb/PassGenie/master/res/words.txt"
    );
    const text = await response.text();
    wlist = text
      .split("\n")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1));
  } catch (error) {
    console.error(error);
    return "Error reading words file";
  }
  let toReturn = [];
  for (let i = 0; i < leng; i++) {
    toReturn.push(wlist[Math.floor(Math.random() * wlist.length)]);
  }
  return toReturn.join("");
}

const select = document.getElementById("select");
const textfield = document.getElementById("textfield");
const addButton = document.getElementById("add");
const list = document.getElementById("list");
const screenHeight = screen.height;
let lis = list.getElementsByClassName("list-item");
let combinedText = "";
let generatedPassword = document.getElementById("generated-password");
let container = document.getElementById("container");
let halfHeight = screenHeight / 2;

let observer = new MutationObserver(function () {
  if (list.children.length >= 20) {
    container.style.overflow = "scroll";
    container.style.height = halfHeight + "px";
    console.log(halfHeight + "px");
  }
});

addButton.addEventListener("click", () => {
  if (
    select.value !== "Custom" &&
    select.value !== "Mirror" &&
    textfield.value !== ""
  ) {
    const item = document.createElement("li");
    textfield.value = textfield.value.replace(/\D/g, "");
    item.classList.add("list-item");
    if (select.value == "RanS") {
      item.innerHTML = `
        ${genRandomSyms(textfield.value)}
        <span class="remove-part">&times;</span>
      `;
    } else if (select.value == "RanN") {
      item.innerHTML = `
        ${genRandomNums(textfield.value)}
        <span class="remove-part">&times;</span>
      `;
    } else if (select.value == "RanL") {
      item.innerHTML = `
        ${genRandomLetters(textfield.value)}
        <span class="remove-part">&times;</span>
      `;
    } else if (select.value == "RanW") {
      genRandomWords(textfield.value).then((result) => {
        item.innerHTML = `
        ${result}
        <span class="remove-part">&times;</span>
      `;
      });
    } else {
      console.log("How did this even happen...?");
      console.error("Wrong selection.");
    }
    list.appendChild(item);
    //textfield.value = "";

    // * Removing the selection may be annoying, so it defaults to Random Symbols
    select.value = "RanS";

    lis = list.getElementsByClassName("list-item");
    combinedText = "";

    for (let i = 0; i < lis.length; i++) {
      combinedText += lis[i].firstChild.textContent.replace(/\s/g, "");
      //console.log(combinedText);
    }
    generatedPassword.textContent = combinedText;

    observer.observe(list, {
      childList: true,
    });

    const crossIcons = document.querySelectorAll(".remove-part");
    crossIcons.forEach((icon) => {
      icon.addEventListener("click", () => {
        icon.parentElement.remove();
      });
    });
  }
});
