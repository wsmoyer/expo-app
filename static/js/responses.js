new Vue({
    el: '#app',
    delimiters: ['[[',']]'],
    data: {
      responses: [],
      questions:[],
      labels:[],
      datasets:[],
     
  },
  mounted: function() {
      var self = this
      var loc = window.location
      var wsStart = 'ws://'
      if (loc.protocol == 'https:'){
          wsStart = 'wss://'
      }
      var endpoint = wsStart + loc.host + loc.pathname
      var socket = new WebSocket(endpoint)
      
      self.handleOpen(socket);

      self.handleMessage(socket,self);

      self.handleClose(socket);

      self.handleError(socket);  

      
 },
  methods: {
      handleOpen:function(socket){
          socket.onopen = function(e){
          socket.send(JSON.stringify({'command':'fetch_responses'}))
          socket.send(JSON.stringify({'command':'fetch_questions'}))
      }
      },
      handleMessage: function(socket,self){
          socket.onmessage = function(e){     
          var msg = JSON.parse(e.data)
            
               if (msg[0].command == 'fetch_questions'){
                self.questions = msg
                self.questions.forEach(q => {
                  var arr_answers = []
                  var arr_count = []
                  q.answers.forEach(a => {
                    arr_answers.push(a.answer)
                    arr_count.push(a.count)
                  })
                    var data = {
                        type: 'bar',
                        data: {
                          labels: arr_answers,
                          datasets: [
                            { // one line graph
                              label: 'Number of Reponses',
                              data: arr_count,
                              backgroundColor: [
                                '#001580',
                                '#6b0080',
                                // '#806b00',
                                '#158000'
                              ],
                              borderColor: [
                                '#001580',
                                '#6b0080',
                                // '#806b00',
                                '#158000'
                              ],
                              borderWidth: 3
                            },
                          ]
                        },
                        options: {
                          responsive: true,
                          lineTension: 1,
                          scales: {
                            yAxes: [{
                              ticks: {
                                beginAtZero: true,
                                padding: 25,
                              }
                            }]
                          }
                        }
                      }
                     
                     
                    var selector = document.getElementById(`${q.question}`)
                    self.createChart(selector,data)
                });
        }
        else if (msg[0].command == 'fetch_responses'){ 
          self.responses = msg
          }
          else {
              self.responses.push(msg[0])
              socket.send(JSON.stringify({'command':'fetch_questions'}))
          }
      }
      },
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

        createChart:function(chartId, chartData) {
            const ctx = chartId.getContext('2d');
            const myChart = new Chart(ctx, {
              type: chartData.type,
              data: chartData.data,
              options: chartData.options,
            });
          }
        }
      
  });