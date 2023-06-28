document.querySelector("#table-input").addEventListener("input", handleSearch);

function handleSearch(event)
{
    const searchValue = event.target.value.toLowerCase(); // Read the search input value and convert to lowercase
    const galleryCards = document.querySelectorAll('.gallery .card'); // Select all of the cards in html

    galleryCards.forEach(cardSelection) // Loop through each card

    function cardSelection(card) 
    {       // Select the card title, file name, description, extension, and created at date
            const title = card.querySelector('.card-title').textContent.toLowerCase();
            const fileName = card.querySelector('.file-name').textContent.toLowerCase();
            const description = card.querySelector('.description').textContent.toLowerCase();
            const extension = card.querySelector('.extension').textContent.toLowerCase();
            const createdAt = card.querySelector('.created-at').textContent.toLowerCase();

            // Hide or show cards based on search input
            if (title.includes(searchValue) || fileName.includes(searchValue) || description.includes(searchValue) || extension.includes(searchValue) || createdAt.includes(searchValue)) 
            {
                card.style.display = ''; // Show the card (default function)
            } 
            else 
            {
                card.style.display = 'none'; // Hide the card
            }
    }
};

