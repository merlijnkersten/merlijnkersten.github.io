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
    const currentYear = today.getFullYear()
    const startNextYear = new Date(currentYear, 3, 21) // 21 April

    if (today < startNextYear) {
        return currentYear - 2018
    }
    else {
        return currentYear - 2018 + 1
    }
}

function formatDate(years) {
    let month = String(today.getMonth() + 1),
        day = String(today.getDate()),
        year = (today.getFullYear() - years)

    if (month.length < 2) {
        month = '0' + month
    }
    if (day.length < 2) {
        day = '0' + day
    }

    return [year, month, day].join('-')
}

function generateURL(year) {
    const githubURL = "/assets/soloespresso"
    return githubURL + formatDate(year) + ".jpg"
}

// Each entry holds the image URL and the full caption (e.g. "27 April 2022").
const photos = []

const dayAndMonth = today.getDate() + ' ' + today.toLocaleString('default', { month: 'long' })

let i = 1 // skip the current year
while (i < yearsSinceStart()) {
    photos.push({
        url: generateURL(i),
        caption: dayAndMonth + ' ' + (today.getFullYear() - i)
    })
    i++
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
