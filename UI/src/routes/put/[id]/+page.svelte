<script>
    import { page } from "$app/state";

let id=page.params.id;  //gets id from the url
let welcome=$state("Add a Note")
    let subtitle="Your comfy corner for all errant thoughts"
    let note=$state(
        {title:"",
        content:""}
    )                            //object to help match the pydantic model
     function clickbutt(){
        console.log("BUTTON WORKED")
        fetch(`http://127.0.0.1:8000/api/notes/${id}`, {method:"PUT", headers: {"Content-Type":"application/json" }, body: JSON.stringify(note)})
        }                  //function for saving changes to note
</script>
<h1>{welcome}</h1>
<h2>{subtitle}</h2>
<div>
   <div>
    <h3>Edit Note:</h3>
    <p>Title: <input type="text" bind:value={note.title}></p>
    <p>Content: <input type="text" bind:value={note.content}></p>
    <p>{note.title}</p>
    <p>{note.content}</p>
    </div>
    <button onclick={clickbutt}>Save</button>
</div>
