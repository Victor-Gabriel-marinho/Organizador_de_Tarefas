const openButton = document.querySelectorAll('.open_modal');

openButton.forEach(button => {
    button.addEventListener('click', ()=>{
        const modalId = button.getAttribute('data-modal');
        const modal = document.getElementById(modalId);

        modal.showModal();
    });
});

const closeButton = document.querySelectorAll('.close_modal');

closeButton.forEach(button => {
    button.addEventListener('click', () =>{
        const modalId = button.getAttribute('data-modal');
        const modal = document.getElementById(modalId);

        modal.close();
    });
});