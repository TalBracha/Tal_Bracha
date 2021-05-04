
fetch('https://reqres.in/api/users?page=2').then
(list => list.json()).then(listUsers => createList(listUsers.data))

function createList(users){
    console.log(users);
    const cMain = document.querySelector("main");
    for(let user of users){
       const section= document.createElement('section') ;
       section.innerHTML = `
           <img src ="${user.avatar}" alt="Pofile Picture"/>
           <div>
             ${user.first_name} ${user.last_name}
              <br>
              <a href="mailto:${user.email}">Send email</a>
           </div> ` ;
        cMain.appendChild(section);
    }
}
