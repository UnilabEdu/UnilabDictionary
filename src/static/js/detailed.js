import { data } from "./data.js";

const cardsWrapper = document.querySelector(".term-cards-wrapper");
let wordsCount = 7;

const weekTerm = data.filter((term) => term.weekTerm);

const dataToRender = data.filter((item) => item.id < 3);
renderData(dataToRender);
if (document.body.offsetWidth < 769) {
  const cards = document.querySelectorAll(".term-card");
  cards.forEach((card) => {
    card.classList.add("fullsize");
  });
}

function renderData(array) {
  if (document.body.offsetWidth < 769) {
    wordsCount = 6;
  }
  if (document.body.offsetWidth < 480) {
    wordsCount = 5;
  }
  array.forEach((element) => {
    cardsWrapper.innerHTML += "";
    // console.log(element.Description)
    const card = document.createElement("div");
    card.setAttribute("class", "term-card");
    cardsWrapper.append(card);
    card.innerHTML = `
        <div class="card-header">
            <span class="term-icon">
                <img src="${element.iconPath}" ../alt="third icon">
            </span>
            <h3 class="term-header-title"><span>${element.titleEng} -</span><span>${element.titleGeo}</span></h3>
        </div>

        <div class="card-body">
            <p class="term-description">${element.Description.split(" ").splice(0, wordsCount).join(" ") + "..."}</p>
        </div>

        <div class="card-footer">
            <div class="hashtag-keywords">
            <a href="dictionary.html"><span>#${element.hashTags[1]}</span></a>
            <a href="dictionary.html"><span>#${element.hashTags[0]}</span></a>
        </div>

        <div class="button-wrapper">
            <a href="#" class="see-details">ნახე სრულად</a>
        </div>
    `;
  });
}
