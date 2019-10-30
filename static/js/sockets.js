
    var loc = window.location
    var wsStart = 'ws://'
    if (loc.protocol == 'https:'){
        wsStart = 'wss://'
    }
    var endpoint = wsStart + loc.host + loc.pathname
    var socket = new WebSocket(endpoint)

    socket.onopen = function(e){
       $( 'form' ).on( 'submit', function(event){
       event.preventDefault();
       var response = event.target.children[2].childNodes[1].value
     
       if (response != '' ){
       var question_id = event.target.children[0].value
       var formData = {
           'message':response,
           'question_id':question_id,
           'command':'handle_submission'
       }
       socket.send(JSON.stringify(formData))
       $(":submit",this).attr("disabled", "disabled")

       $(this)[0].reset()
       $(":submit",this)[0].value = 'Submitted';

    } else {
        var errors = $('#errors')
        errors.append(`<li class='text-danger'>Please fill in this field</li>`)

    }       
       });
    }

    socket.onclose = function(e){
       console.log('close',e)

    }
    socket.onerror = function(e){
        console.log('error',e)
    }


