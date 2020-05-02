var selectFile;
$('#id_article_image').change(function(event){
     selectFile = event.target.files[0];

})

$('#submit').click(function () {
    var filename = selectFile.name;
    var storageRef = firebase.storage().ref('/article_images/' + filename);
    var uploadTask = storageRef.put(selectFile);
    uploadTask.on('state_changed', function (snapshot) {
    }, function(error){

    }, function() {
        var downloadURl = uploadTask.snapshot.downloadURl;
        console.log(downloadURl);
    })
})