/* used: https://stackoverflow.com/questions/39919038/javascript-changing-between-three-images-on-a-button-click, answer by https://stackoverflow.com/users/949476/dfsq
Goal: on clicking on image, cycle through the images of the previous years
Steps: 
    1) find how many full years have passes since the start of the project (22 April 2018),
    2) create an array with the URLs to the image of each year of (for the current date),
    3) change the image URL and caption date in the HTML code.

Todo: currently only shows images, at least two entries were videos and one had audio embedded in the image (edge cases). Temporary solution: show first frame of the video as a plain image.
*/


let today = new Date()

function yearsSinceStart() {
    // return the number of full years since the start of the project (21 April 2018).
    const currentYear = today.getFullYear()

    const startNextYear = new Date(currentYear, 3, 21) // Every year on 21 April

    if (today < startNextYear) {
        // currentDate is before 21 April
        //return currentYear - 2018
        lastYear = 2019
    }
    else {
        // currentDate is on or after 21 April
        //return currentYear - 2018 + 1
        lastYear = 2018
    }

    const yearsArray = []
    let year = currentYear - 1
    while (year >= lastYear) {
        yearsArray.push(year)
        year--
    }

    return yearsArray
}

function formatDate(year) {
    // returns the date in the same format as the Github image URLs
    let month = String(today.getMonth() + 1),
        day = String(today.getDate()),
        year = year

    if (month.length < 2) {
        month = '0' + month
    }
    if (day.length < 2) {
        day = '0' + day
    }

    return [year, month, day].join('-')
}


function generateSoloespressoURL(year) {
    // generates URL to soloespresso images in assets folder for a given year.
    return "/assets/soloespresso" + formatDate(year) + ".jpg"
}

function inNerdonanislandDates(date) {
    // check to see if date is in Nerdonanisland dates
    year = today.getFullYear()
    const startDate = new Date([year, '07', '30'].join('-')).getTime();
    const endDate = new Date([year, '12', '20'].join('-')).getTime();
    return date >= startDate && date <= endDate;
}

function generateNerdonanislandURL() {
    // generate URL to Nerdonanisland image in the assets folder
    return "/assets/nerdonanisland" + formatDate(2017) + ".jpg"
}

// initialise an empty array which will be populated with image URLs.
const imageURLs = []

for (year in yearsArray) {
    let url = generateSoloespressoURL(year)
    imageURLs.push(url)
}

if (inNerdonanislandDates(today) = true) {
    let url = generateNerdonanislandURL()
    imageURLs.push(url)
}

// https://raw.githubusercontent.com/merlijnkersten/merlijnkersten.github.io/master/assets/soloespresso-1651065564681-04-27.jpg



let num = 0

// This function cycles through the imageURLs array by taking the modulo of the num iterator divided by the length of the imageURLs array.
function imageSequence() {
    document.getElementById('image').src = imageURLs[num++ % imageURLs.length]
}

imageSequence()

document.getElementById('image').addEventListener('click', imageSequence)

// Print today's date below the picture in dd mmmm format.
//let date = today.getDate() +' ' + today.toLocaleString('default', { month: 'long' })

document.querySelector("#date").innerText = date

console.log("thanks Fonsi")