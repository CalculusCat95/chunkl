function fileLoad(){
  const val = document.getElementById('open').files[0];
  filereader = new FileReader();
  filereader = filereader.readAsDataUrl(val);
  document.getElementById('chunkldiv').innerHTML(filereader);
}
