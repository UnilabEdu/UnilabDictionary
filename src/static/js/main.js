import { data } from "./data.js";

const cardsWrapper = document.querySelector(".term-cards-wrapper");
let wordsCount = 7;

const weekTermTitleEnd = document.querySelector(".term-title strong");
const weekTermTitleGeo = document.querySelector(".term-title span");
const weekTermDesc = document.querySelector(".week-term-description");
const firstHashtag = document.querySelector(".hashtag-1");
const secondHashtag = document.querySelector(".hashtag-2");
const weekTerm = data.filter((term) => term.weekTerm);
weekTermTitleEnd.textContent = weekTerm[0].titleEng;
weekTermTitleGeo.textContent = weekTerm[0].titleGeo;
weekTermDesc.textContent =
  weekTerm[0].Description.split(" ").splice(0, 11).join(" ") + "...";
firstHashtag.textContent = "#" + weekTerm[0].hashTags[0];
secondHashtag.textContent = "#" + weekTerm[0].hashTags[1];
console.log(weekTerm);
const dataToRender = data.filter((item) => item.id < 3);
// renderData(dataToRender);
if (document.body.offsetWidth < 769) {
  const cards = document.querySelectorAll(".term-card");
  cards.forEach((card) => {
    card.classList.add("fullsize");
  });
}

console.log(document.location.pathname);

// import { renderData } from "./dictionary.js";
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




const search = document.querySelector('#main-search')
search.addEventListener('input', (e) => {
    const filteredData = data.filter(item => item.titleEng.toLowerCase().includes(e.target.value.toLowerCase()) || item.titleGeo.includes(e.target.value))
  console.log(filteredData);












    // if(filteredData.length < 10 && filteredData.length !== 0) {
    //     notFoundMessage.style.display = 'none'
    //     searchCounter(filteredData)
    //     paginationRender(filteredData)
    //     if(filteredData.length === 1) {
    //         cardsWrapper.style.justifyContent = 'flex-start'
    //     }
    //     paginationWrapper.style.display = 'block'
    // }else if (filteredData.length == 0){
    //     notFoundMessage.style.display = 'flex'
    //     searchCounter(filteredData)
    //     paginationWrapper.style.display = 'none'
    // }
    // if (e.target.value == '') {
    //     paginationRender(filteredData)
    //     notFoundMessage.style.display = 'none'
    //     paginationWrapper.style.display = 'block'
    //     messageWrapper.style.display = 'none'
    // }else if (e.target.value !== '' && filteredData.length >= 10){
    //     searchCounter(filteredData)
    //     paginationRender(filteredData)
    //     notFoundMessage.style.display = 'none'

    // }
});