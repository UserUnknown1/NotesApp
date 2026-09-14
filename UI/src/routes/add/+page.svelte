<script>
    import { json } from "@sveltejs/kit";

    let welcome=$state("Add a Note")
    let subtitle="Your comfy corner for all errant thoughts"
    let newNote=$state(
        {title:"",
        content:""}
    )
     function clickbutt(){
        fetch("http://127.0.0.1:8000/api/notes/add", {method:"POST", headers: {"Content-Type":"application/json" }, body: JSON.stringify(newNote)})
        }
</script>
<h1>{welcome}</h1>
<h2>{subtitle}</h2>
<div>
   <div>
    <h3>New Note:</h3>
    <p>Title: <input type="text" bind:value={newNote.title}></p>
    <p>Content: <input type="text" bind:value={newNote.content}></p>
    <p>{newNote.title}</p>
    <p>{newNote.content}</p>
    </div>
    <button onclick={clickbutt}>Add Note</button>
</div>
