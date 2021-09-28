function showDropdown(id) {
  dropdown_ids = [0, 1, 2, 3, 4]
  dropdown_ids.forEach(id => {
    document.getElementById(`myDropdown-${id}`).classList.remove("show");
  })
  document.getElementById(`myDropdown-${id}`).classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropdown-btn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}