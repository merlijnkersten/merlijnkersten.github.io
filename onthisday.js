/* used: https://stackoverflow.com/questions/39919038/javascript-changing-between-three-images-on-a-button-click, answer by https://stackoverflow.com/users/949476/dfsq
Goal: on clicking on image, cycle through the images of the previous years
Steps: 
    1) find how many full years have passes since the start of the project (22 April 2018 for soloespresso,  30 July until 20 December 2017 for nerdonanisland),
    2) create an array with the URLs to the image of each year (for the current date),
    3) change the image URL and caption date in the HTML code.

Todo: currently only shows images, at least two entries were videos and one had audio embedded in the image (edge cases). Temporary solution: show first frame of the video as a plain image.
*/

let today = new Date()

function yearsSinceStart() {
    // number of full years since the start of the project (21 April 2018).
    const currentYear = today.getFullYear()
    const startNextYear = new Date(currentYear, 3, 21) // 21 April

    if (today < startNextYear) {
        return currentYear - 2018
    }
    else {
        return currentYear - 2018 + 1
    }
}

function formatDate(year) {
    // returns the date for the given (absolute) year in the same format as the image URLs
    let month = String(today.getMonth() + 1),
        day = String(today.getDate())

    if (month.length < 2) {
        month = '0' + month
    }
    if (day.length < 2) {
        day = '0' + day
    }

    return [year, month, day].join('-')
}

function generateURL(prefix, year) {
    // generates URL to the image in the assets folder for a given prefix and year.
    return "/assets/" + prefix + formatDate(year) + ".jpg"
}

const dayAndMonth = today.getDate() + ' ' + today.toLocaleString('default', { month: 'long' })

function makePhoto(prefix, year) {
    return {
        url: generateURL(prefix, year),
        caption: dayAndMonth + ' ' + year
    }
}

// Each entry holds the image URL and the full caption (e.g. "27 April 2022").
const photos = []

// Soloespresso: one photo per year since 2018 (skip the current year).
let i = 1
while (i < yearsSinceStart()) {
    photos.push(makePhoto("soloespresso", today.getFullYear() - i))
    i++
}

// Nerdonanisland: only has photos from 30 July to 20 December 2017.
// Compare today's day and month against that range, using 2017 as a stand-in year.
const dayIn2017 = new Date(2017, today.getMonth(), today.getDate())
const nerdStart = new Date(2017, 6, 30)  // 30 July 2017
const nerdEnd = new Date(2017, 11, 20)   // 20 December 2017

if (dayIn2017 >= nerdStart && dayIn2017 <= nerdEnd) {
    photos.push(makePhoto("nerdonanisland", 2017))
}

let num = 0

function imageSequence() {
    const photo = photos[num++ % photos.length]
    document.getElementById('image').src = photo.url
    document.querySelector("#date").innerText = photo.caption
}

imageSequence()

document.getElementById('image').addEventListener('click', imageSequence)

console.log("thanks Fonsi and Claude")
