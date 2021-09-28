var input = document.getElementById('file-input');
var uploadArea = document.getElementById('file-upload-area');
var fileName = document.getElementById('file-list');

uploadArea.addEventListener('dragover', (event) => {
  event.preventDefault();
  uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', (event) => {
  event.preventDefault();
  uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (event) => {
  event.preventDefault();
  uploadArea.classList.remove('dragover');
  var files = event.dataTransfer.files;
  input.files = files;
  console.log(input.files)
  // if(files.length > 1) {
  //   fileName.innerHTML = "<span class='file-name'>" + files.length + "files" + '</span>';
  // } else {
  //   fileName.innerHTML = "<span class='file-name'>" + files[0].name + '</span>';
  // }
  for (var i = 0, f; file = files[i]; i++) {
    fileName.innerHTML += "<span class='file-name'>" + file.name + "files" + '</span>';
  }
});

input.addEventListener('change', (event) => {
  event.preventDefault();
  var files = input.files;
  if(files.length > 1) {
    fileName.innerHTML = files.length + "files";
  } else {
    fileName.innerHTML = files[0].name;
  }
});
