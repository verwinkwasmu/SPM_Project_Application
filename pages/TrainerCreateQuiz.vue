<template>
    <div>
        <TrainerHeader/>
        <section id="team" class="team section-bg">
            <div class="" data-aos="fade-up">
                <div class="section-title">
                  
                    <h2>Fundamentals of Xerox WorkCentre 7845 (Quiz)</h2>

                    <div class="row">
                        <div class="col-lg-8" id="TrainerViewCourseDetails" style="padding-bottom: 40px">                                        
                                <div class="member-info" id="question">
                                    <div>
                                        <div class="float-container">
    
                                            <div id="app" class="">
                                                <h3>Create your True/False or Multiple-Choice Question here</h3>
                                                <div id="div2">
                                                    <label for="question">Type your question: </label>
                                                    <textarea v-model="question" id="question" cols="80" rows="1"></textarea>
                                                </div>
                                                
                                                <br>
                                                    <div id="div1">
                                                    <label for="option1">Option 1: </label>
                                                    <input type="text" v-model="option1" />
                                                    </div>
                                                    <br>

                                                    <div id="div1">
                                                    <label for="option2">Option 2: </label>
                                                    <input type="text" v-model="option2">
                                                    </div>
                                                    <br>

                                                    <div id="div1">
                                                    <label for="option1">Option 3: </label>
                                                    <input type="text" class="tb" v-model="option3" />
                                                    </div>
                                                    <br>

                                                    <div id="div1">
                                                    <label for="option2">Option 4: </label>
                                                    <input type="text" v-model="option4">
                                                    </div>
                                                    <br>


                                                    <div id="div3">
                                                    <label for="correctOption">Answer: </label>
                                                    <input type="text" v-model="correctOption">
                                                    </div>
                                                    <br>
                                                    
                                                <hr>

                                                <h3>Preview Question</h3>
                                                <!-- <question :question="question" :options="options"></question> -->
                                                <h5>{{question}}</h5>
                                                <label for="option1"><input name="answers" type="radio" :val="option1"> {{option1}}</label>
                                                <br>
                                                <label for="option2"><input name="answers" type="radio" :val="option2"> {{option2}}</label>
                                                <br>
                                                <label for="option3"><input name="answers" type="radio" :val="option1"> {{option3}}</label>
                                                <br>
                                                <label for="option4"><input name="answers" type="radio" :val="option2"> {{option4}}</label>
                                                <br>
                                                
                                                <br>
                                                <br>

                                                    
                                                <div>
                                                    <label for="graded"><input name="graded" type="radio" value="Yes" v-model="graded"> Select if the quiz is graded </label> 
                                                </div>
                                                <br>
                                                    

                                                    <label for="time">Enter duration of the quiz (in minutes): </label>
                                                    <input type="number" min= "1" v-model="time">

                                            </div>
                                            
                                        </div>                                    
                                    </div>                                                                                                                            
                                </div>
                            </div>
                        </div>

  
                    </div>
                </div>
                
                <div class="buttongroup">
                    <div class="TrainerCreateQuiz">
                        <a href="" class="TrainerCreateQuiz-btn" @click="testing">Add Question</a>
                    </div>

                    <div class="TrainerCancelQuiz">
                        <a href="TrainerCancelQuiz" class="TrainerCancelQuiz-btn">Cancel</a>
                    </div>
                </div>
                   

        </section>
    </div>
</template>



<script>
  export default {
    data: () => ({
        question: 'Your Question',
        option1: '',
        option2: '',
        option3: '',
        option4: '',
        correctOption: '',
        time: 1,
        graded: '',
    }),
        
    methods: {
        testing: function(){
            if (this.option1 != "" && this.option2 != ""){
                console.log('yay')
                console.log(this.option1)
                console.log(this.option2)
            }
            else {
                console.log('Please enter an option')
            }
        },
    }
  };

</script>

