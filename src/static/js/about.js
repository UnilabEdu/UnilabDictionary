import "./slick/slick.min.js";
import "//code.jquery.com/jquery-migrate-1.2.1.min.js";
import { members } from "./data.js";

const teamWrapper = document.querySelector(".meet-team-wrapper");
const personName = document.querySelectorAll(".person-name");
const personLastname = document.querySelectorAll(".person-lastname");
const personLPosition = document.querySelectorAll(".person-position");

renderMembers(members, teamWrapper);

function renderMembers(array, wrapper) {
  wrapper.innerHTML = "";
  array.forEach((el) => {
    wrapper.innerHTML += `
                <div class="slick-slide-wrapper" style="background-image: url(${el.memberImagePath})"><div class="about-person"><span class="person-name">${el.memberName}</span><span class="person-lastname">${el.memberLastname}</span><span class="person-position">${el.memberPosition}</span></div></div>
            `;
  });
  // <img src=${el.memberImagePath} alt="team member">
}
$(".meet-team-wrapper").slick({
  // autoplay: true,
  infinite: true,
  dots: false,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 2,
  centerMode: false,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 2,
        infinite: true,
        dots: true,
      },
    },
    {
      breakpoint: 769,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        infinite: true,
        dots: true,
      },
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
      },
    },
    {
      breakpoint: 480,
      settings: {
        centerMode: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
      },
    },
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ],
});
