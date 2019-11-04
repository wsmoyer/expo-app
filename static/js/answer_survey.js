
new Vue({
    el: '#app',
    delimiters: ['[[',']]'],
    data: {
        questions:[]
  },
  mounted:function(){
  var self = this
  var loc = window.location
  var wsStart = 'ws://'
  if (loc.protocol == 'https:'){
      wsStart = 'wss://'
  }
  var endpoint = wsStart + loc.host + loc.pathname
  var socket = new WebSocket(endpoint)

  socket.onopen = function(e){
      socket.send(JSON.stringify({'command':'fetch_questions'}))
      self.handleMessage(socket,self)
      self.handleSubmission(socket)

  }
  self.handleClose(socket)

  self.handleError(socket)
  },
  methods: {
      handleClose: function(socket,self){
          socket.onclose = function(e){
          console.log('close',e)
      }
      },
      handleError:function(socket){
          socket.onerror = function(e){
          console.log('error',e)
      }
      },
      handleSubmission:function(socket){
          $( 'form' ).on( 'submit', function(event){
          event.preventDefault();
          var response = event.target.children[2]
          var selectedRes = response.options[response.selectedIndex].value;

          if (response != '' ){
          var question_id = event.target.children[0].value
          var formData = {
              'message':selectedRes,
              'question_id':question_id,
              'command':'handle_submission'
          }
          socket.send(JSON.stringify(formData))
          $(":submit",this).attr("disabled", "disabled")

          // $(this)[0].reset()
          $(":submit",this)[0].value = 'Submitted';

          } else {
              // var errors = $('#errors')
              // errors.append(`<li class='text-danger'>Please fill in this field</li>`)
              // errors.fadeIn('slow').delay(1000).hide(0);
                  }       
              });
          },
          handleMessage:function(socket,self){
              socket.onmessage = function(e){     
              var msg = JSON.parse(e.data)
              self.questions = msg
              }
          }  
  }
  });
