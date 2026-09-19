<script>
    import { goto } from "$app/navigation";
import { json } from "@sveltejs/kit";
    import { onMount } from "svelte";

    let welcome=$state("My Notes App")
    let subtitle="Your comfy corner for all errant thoughts"
    
    let allNotes=$state([])
    onMount(async()=>{
    let response= await fetch("http://127.0.0.1:8000/api/notes/")
    let  newNote=await response.json()
    allNotes=newNote
    }  )
    let delNote = async (id) => {
    let response = await fetch(`http://127.0.0.1:8000/api/notes/${id}`, {
        method: "DELETE"
    })

    if (response.ok) {
        allNotes = allNotes.filter(note => note.id !== id)
    }
}

    let editNote=(id)=>{goto(`/put/${id}`)}
</script>
<div class="page">
<h1>
    {welcome}
</h1>
<div class="h2-con">
<h2 class="head">{subtitle}</h2>
</div>
<div>
   <div>
    <h3>All Notes</h3>
   
    </div>
    
</div>

<div class= note>
    <p>All Notes</p>
    <table>
        <tbody>
        {#each allNotes as note}
        
        <tr>
            <td>{note.title}</td>
            <td>{note.content}</td>
            <td><button onclick={()=>editNote(note.id)}>Edit</button></td> 
            <td><button onclick={()=>delNote(note.id)}>Delete</button></td> 
        </tr>
        {/each}
        </tbody>
    </table>
    <div class="butt">
    <button class="add-button", onclick={() => goto('/add')}>Add Note</button>
    </div>
    </div>
    </div>



<style>
:global(body)
 {
    margin:0;
    min-height: 100vh;
    font-family: 'Nunito', sans-serif;
    background: #171022;
    color: #f8eaf5;
}

/* Main page */

.page {
    min-height: 100vh;
    padding: 40px;
    box-sizing: border-box;
}

/* Header */

h1 {
    margin: 0 auto 35px;
    padding: 18px 30px;
    max-width: 800px;

    text-align: center;
    font-size: 42px;
    color: #ff9edb;

    background: #241532;
    border: 2px solid #8e4585;
    border-radius: 18px;

    box-shadow: 0 0 25px rgba(255, 105, 190, 0.18);
}

/* Add note button */

:global(button) {
    font-family: inherit;
    font-size: 16px;
    font-weight: bold;

    padding: 10px 18px;
    border: none;
    border-radius: 10px;

    background: #e98bc7;
    color: #241532;

    cursor: pointer;
    transition: 0.2s ease;
}

button:hover {
    background: #ffb5e3;
    transform: translateY(-2px);
}

button:active {
    transform: translateY(0);
}

/* Notes container */

.notes {
    max-width: 850px;
    margin: 0 auto;

    display: flex;
    flex-direction: column;
    gap: 18px;
}

/* Individual note */

.note {
    padding: 22px;

    background: #21142d;
    border: 1px solid #5f3565;
    border-radius: 16px;

    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);

    transition: 0.2s ease;
}

.note:hover {
    border-color: #c76bb0;
    box-shadow: 0 0 20px rgba(230, 115, 190, 0.15);
    transform: translateY(-2px);
}

/* Note title */

.note h2 {
    margin: 0 0 10px;

    color: #ffacd9;
    font-size: 23px;
}

/* Note content */

.note p {
    margin: 0 0 18px;

    color: #dfcfe0;
    line-height: 1.6;
}

/* Links */

a {
    color: #ff9edb;
    text-decoration: none;
    font-weight: bold;
}

a:hover {
    color: #ffc4e7;
    text-decoration: underline;
}

/* ------------------------------
   NOTE FORM
   ------------------------------ */

form {
    max-width: 700px;
    margin: 0 auto;

    padding: 28px;

    background: #21142d;
    border: 1px solid #6d3c72;
    border-radius: 18px;

    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

input,
textarea {
    width: 100%;
    box-sizing: border-box;

    margin-bottom: 18px;
    padding: 13px 15px;

    font-family: inherit;
    font-size: 16px;

    color: #f8eaf5;
    background: #171022;

    border: 1px solid #69406d;
    border-radius: 10px;

    outline: none;
}

textarea {
    min-height: 180px;
    resize: vertical;
}

input:focus,
textarea:focus {
    border-color: #e98bc7;
    box-shadow: 0 0 10px rgba(233, 139, 199, 0.2);
}


@media (max-width: 600px) {
    .page {
        padding: 20px;
    }

    h1 {
        font-size: 32px;
        padding: 15px;
    }

    .note {
        padding: 18px;
    }
}
</style>
