import { data } from "./data.js";
import 'https://unpkg.com/swiper@8/swiper-bundle.min.js';

const alphabetArrGeo = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ო', 'პ', 'ჟ', 'რ', 'ს', 'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']
const alphabetArrEng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
let wordsCount = 7;
const cardsWrapper = document.querySelector('.term-cards-wrapper');

const swiperWrapper = document.querySelector('.swiper-wrapper');
const alphabetWrapper = document.querySelector('.alphabet-wrapper')
const alphabetSwitcher = document.querySelector('.alphabet-switcher')
const searchFilter = document.querySelector('#filter')
const resultCounter = document.querySelector('.search-result-counter')
const messageWrapper = document.querySelector('.counter-wrapper')
const notFoundMessage = document.querySelector('.not-found-message-wrapper')
const paginationWrapper = document.querySelector('.pagination')
let termsPerPage = 9
let paginationResult;
const selects = document.querySelectorAll('#dropdown-wrapper .select select')
let usp = new URLSearchParams()
if (document.body.offsetWidth < 480) {
    termsPerPage = 3
} else if (document.body.offsetWidth < 991) {
    termsPerPage = 6

} else {
    termsPerPage = 9

}
const swiper = new Swiper('.swiper', {
    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    // And if we need scrollbar
    scrollbar: {
        el: '.swiper-scrollbar',
    },
    slidesPerView: 10,
    slidesPerGroup: 7,
    freeMode: true,
});


// initiate first page on window load
window.onload = () => {
    swiper.update();
    // document.querySelector('.page-number').click()
}
// initiate first page on window load
// generating 9 cards per page
//paginationRender(data)
function paginationRender(arr) {
    paginationWrapper.innerHTML = '';
    const roundedTermsNum = Math.ceil(arr.length / termsPerPage)
    const doubleLeft = document.createElement('span')
    doubleLeft.setAttribute('class', 'pagination-double-left-arrow')
    doubleLeft.innerHTML =
        `   <span class="double-arrows-wrapper">
            <svg xmlns="http://www.w3.org/2000/svg" width="12.51" height="8.893" viewBox="0 0 12.51 8.893">
            <g id="noun_Arrow_2884045" transform="translate(12.51) rotate(90)">
                <path id="Path_3" data-name="Path 3" d="M8.307,12.51.207,6.66a.5.5,0,0,1,0-.81L8.307,0l.586.811L1.354,6.255,8.893,11.7Z" transform="translate(0 0)" fill="#8a8fa3" opacity="0.63"/>
            </g>
        </svg><svg xmlns="http://www.w3.org/2000/svg" width="12.51" height="8.893" viewBox="0 0 12.51 8.893">
        <g id="noun_Arrow_2884045" transform="translate(12.51) rotate(90)">
            <path id="Path_3" data-name="Path 3" d="M8.307,12.51.207,6.66a.5.5,0,0,1,0-.81L8.307,0l.586.811L1.354,6.255,8.893,11.7Z" transform="translate(0 0)" fill="#8a8fa3" opacity="0.63"/>
        </g>
    </svg>
            </span>
            `
    paginationWrapper.append(doubleLeft)
    const leftArrow = document.createElement('span')
    leftArrow.setAttribute('class', 'pagination-left-arrow')
    leftArrow.innerHTML =
        `
            <svg xmlns="http://www.w3.org/2000/svg" width="12.51" height="8.893" viewBox="0 0 12.51 8.893">
                <g id="noun_Arrow_2884045" transform="translate(12.51) rotate(90)">
                    <path id="Path_3" data-name="Path 3" d="M8.307,12.51.207,6.66a.5.5,0,0,1,0-.81L8.307,0l.586.811L1.354,6.255,8.893,11.7Z" transform="translate(0 0)" fill="#8a8fa3" opacity="0.63"/>
                </g>
            </svg>
            `
    paginationWrapper.append(leftArrow)
    if (roundedTermsNum >= 1) {
        for (let i = 1; i <= roundedTermsNum; i++) {
            const pageNumber = document.createElement('span')
            pageNumber.setAttribute('class', 'page-number')
            pageNumber.innerText = i
            paginationWrapper.append(pageNumber)
            pageNumber.addEventListener('click', function () {
                document.querySelectorAll('.page-number').forEach(el => el.classList.remove('active-page'))
                this.classList.add('active-page')
                const pageNum = +this.innerText
                const startPoint = (pageNum - 1) * termsPerPage
                const endPoint = startPoint + termsPerPage
                paginationResult = arr.slice(startPoint, endPoint)
                // cardsWrapper.innerHTML = ''
                // renderData(paginationResult)
            })
        }
        document.querySelector('.page-number').click()
    }
    const rightArrow = document.createElement('span')
    rightArrow.setAttribute('class', 'pagination-right-arrow')
    rightArrow.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" width="12.51" height="8.893" viewBox="0 0 12.51 8.893">
                <g id="noun_Arrow_2884045" transform="translate(0 8.893) rotate(-90)">
                    <path id="Path_3" data-name="Path 3" d="M8.307,0,.207,5.85a.5.5,0,0,0,0,.81l8.1,5.85.586-.811L1.354,6.255,8.893.81Z" fill="#8a8fa3" opacity="0.63"/>
                </g>
            </svg>
            `
    paginationWrapper.append(rightArrow)
    leftArrow.addEventListener('click', () => {
        console.log('left clicked')
    })
    rightArrow.addEventListener('click', () => {
        console.log('right clicked')
    })
    const doubleRight = document.createElement('span')
    doubleRight.setAttribute('class', 'pagination-double-right-arrow')
    doubleRight.innerHTML =
        `   <span class="double-arrows-wrapper">
            <svg xmlns="http://www.w3.org/2000/svg" width="12.51" height="8.893" viewBox="0 0 12.51 8.893">
            <g id="noun_Arrow_2884045" transform="translate(0 8.893) rotate(-90)">
                <path id="Path_3" data-name="Path 3" d="M8.307,0,.207,5.85a.5.5,0,0,0,0,.81l8.1,5.85.586-.811L1.354,6.255,8.893.81Z" fill="#8a8fa3" opacity="0.63"/>
            </g>
        </svg><svg xmlns="http://www.w3.org/2000/svg" width="12.51" height="8.893" viewBox="0 0 12.51 8.893">
        <g id="noun_Arrow_2884045" transform="translate(0 8.893) rotate(-90)">
            <path id="Path_3" data-name="Path 3" d="M8.307,0,.207,5.85a.5.5,0,0,0,0,.81l8.1,5.85.586-.811L1.354,6.255,8.893.81Z" fill="#8a8fa3" opacity="0.63"/>
        </g>
    </svg>
            </span>
            `
    paginationWrapper.append(doubleRight)
}
// generating 9 cards per page
// generate alphabet for desktop
alphabetGenerator(alphabetArrGeo)
// generate alphabet for desktop
// initiate slider
swiperInit(alphabetArrGeo)

swiperWrapper.childNodes.forEach(letter => {
    //add class for Transform ToLowerCase
    letter.classList.add('alphabet-toLowerCase')
});
// initiate slider
// adding active class to first letter
alphabetWrapper.childNodes[1].classList.add('active-letter')
swiperWrapper.childNodes[0].classList.add('active-letter')
// adding active class to first letter
lettersOnClick('.letter-box')
const switchFace = document.querySelector('.switch-face')
const background = document.querySelector('.alphabet-bg')
const switchTextEng = 'ENG'
const switchTextGeo = 'ქარ'
switchFace.innerText = switchTextEng
background.addEventListener('click', (e) => {
    e.stopImmediatePropagation()
    alphabetSwitcher.click()
})
alphabetSwitcher.addEventListener('click', (e) => {
    e.stopImmediatePropagation()
    if (switchFace.innerText == switchTextEng) {
        switchFace.innerText = switchTextGeo
        alphabetWrapper.innerText = ''
        alphabetGenerator(alphabetArrEng)

        console.log(document.body.offsetWidth)
        if (document.body.offsetWidth < 570) {
            alphabetSwitcher.style.transform = 'translateX(25px)'
        } else {
            alphabetSwitcher.style.transform = 'translateX(34px)'
        }
        //add class for Transform ToUpperCase
        lettersOnClick('.letter-box')
        swiperInit(alphabetArrEng)
        alphabetWrapper.childNodes[0].classList.add('active-letter')
        swiperWrapper.childNodes[0].classList.add('active-letter')
        swiperWrapper.childNodes.forEach(letter => {
            letter.classList.add('alphabet-toUpperCase')
        });
    }
    else {
        switchFace.innerText = switchTextEng
        alphabetWrapper.innerText = ''
        alphabetGenerator(alphabetArrGeo)

        alphabetSwitcher.style.transform = 'translateX(0px)'
        lettersOnClick('.letter-box')
        swiperInit(alphabetArrGeo)
        alphabetWrapper.childNodes[0].classList.add('active-letter')
        swiperWrapper.childNodes[0].classList.add('active-letter')
        swiperWrapper.childNodes.forEach(letter => {
            //add class for Transform ToLowerCase
            letter.classList.add('alphabet-toLowerCase')
        });
    }
    swiper.update();
    swiper.slideTo(0, 0)

})
searchFilter.addEventListener('change', () => {
    const searchFilterData = data.filter(item => item.keyword == searchFilter.value)
    searchCounter(searchFilterData)
    if (searchFilter.value !== 'default') {
        cardsWrapper.innerHTML = ''
        //paginationRender(searchFilterData)
    }
})

const search = document.querySelector('#search')
search.addEventListener('input', (e) => {
    // cardsWrapper.innerHTML = ''
    const filteredData = data.filter(item => item.titleEng.toLowerCase().includes(e.target.value.toLowerCase()) || item.titleGeo.includes(e.target.value))
    if (filteredData.length < 10 && filteredData.length !== 0) {
        notFoundMessage.style.display = 'none'
        searchCounter(filteredData)
        //paginationRender(filteredData)
        if (filteredData.length === 1) {
            cardsWrapper.style.justifyContent = 'flex-start'
        }
        paginationWrapper.style.display = 'block'
    } else if (filteredData.length == 0) {
        notFoundMessage.style.display = 'flex'
        searchCounter(filteredData)
        paginationWrapper.style.display = 'none'
    }
    if (e.target.value == '') {
        paginationRender(filteredData)
        notFoundMessage.style.display = 'none'
        paginationWrapper.style.display = 'block'
        messageWrapper.style.display = 'none'
    } else if (e.target.value !== '' && filteredData.length >= 10) {
        searchCounter(filteredData)
        //paginationRender(filteredData)
        notFoundMessage.style.display = 'none'

    }
});

function searchCounter(arr) {
    if (arr != null) {
        messageWrapper.style.display = 'block'
        resultCounter.innerText = arr.length
    }
}
async function alphabetGenerator(alphabetArray) {
    if (alphabetArray[0] == alphabetArrGeo[0]) {
        alphabetArray.forEach((letter) => {
            const letterSpan = document.createElement('span')
            letterSpan.setAttribute('class', 'letter-box geo')
            letterSpan.innerText = letter
            alphabetWrapper.append(letterSpan)
            letterSpan.addEventListener('click', (e) => {
                console.log(e.target);
            })
        })
    } else {
        alphabetArray.forEach((letter) => {
            const letterSpan = document.createElement('span')
            letterSpan.setAttribute('class', 'letter-box')
            letterSpan.innerText = letter.toUpperCase()
            alphabetWrapper.append(letterSpan)
            letterSpan.addEventListener('click', (e) => {
                console.log(e.target);
            })
        })
    }
}
function lettersOnClick(someClass) {
    const letterBoxes = document.querySelectorAll(someClass)
    letterBoxes.forEach(letterBox => {
        letterBox.addEventListener('click', function () {
            letterBoxes.forEach(letter => letter.classList.remove('active-letter'))
            letterBox.classList.add('active-letter')
        })
    })
}
function swiperInit(arr) {
    swiperWrapper.innerHTML = '';
    arr.forEach(el => {
        const upperCase = el.toUpperCase()
        const letter = document.createElement('div')
        letter.setAttribute('class', 'swiper-slide')
        letter.innerText = upperCase
        swiperWrapper.append(letter)
        lettersOnClick('.swiper-slide')
    })
}





// export function renderData(array) {
//     if (document.body.offsetWidth < 769) {
//         wordsCount = 6

//     }
//     if (document.body.offsetWidth < 480) {
//         wordsCount = 5
//     }
//     array.forEach((element) => {
//         cardsWrapper.innerHTML += ''
//         // console.log(element.Description)
//         const card = document.createElement('div')
//         card.setAttribute('class', 'term-card')
//         cardsWrapper.append(card)
//         card.innerHTML = `
//                       <div class="card-header">
//                           <span class="term-icon">
//                               <img src="${element.iconPath}" ../alt="third icon">
//                           </span>
//                           <h3 class="term-header-title"><span>${element.titleEng} -&nbsp;</span><span>${element.titleGeo}</span></h3>
//                       </div>
//                       <div class="card-body">
//                           <p class="term-description">${element.Description.split(' ').splice(0, wordsCount).join(' ') + "..."}</p>
//                       </div>
//                       <div class="card-footer">
//                           <div class="hashtag-keywords">
//                             <a href="dictionary.html"><span>#${element.hashTags[1]}</span></a>
//                             <a href="dictionary.html"><span>#${element.hashTags[0]}</span></a>
//                           </div>
//                           <div class="button-wrapper">
//                               <a href="#" class="see-details">ნახე სრულად</a>
//                           </div>
//                       </div>
//         `
//     })
// }




function urlUpdate(item){
    item.addEventListener("input", function(e) {
        const selectedValue = e.target.value;
        const itemID = this.getAttribute('id')
        usp.set(itemID, selectedValue)
        const newUrl = window.location.pathname + '?' + usp.toString();
        window.history.pushState({},'', newUrl)
      });
}

    // updates url by filter and sort
function filterSort(){
    selects.forEach(function (item) {
            urlUpdate(item)
    })
}
filterSort();

    // updates url by input
function searchFunc(text){
    urlUpdate(text)
}
searchFunc(search)