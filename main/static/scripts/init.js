function init(page){
    var pages = ['verschwinden', 'lehramtsschule', 'ayotzinapa', 'students', 'contact', 'quellen']
    for (i=0; i++; i< 6){
        document.getElementById(pages[i]).classList.remove('opacity');
    }
    document.getElementById(page).classList.add('opacity');

}