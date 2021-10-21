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
                                            <div class="float-child-left">
                                                <label for="question">Question 1: </label>
                                            </div>
                                            <div class="float-child-right">
                                                <b-form-input v-model="questionTF" placeholder="Enter question"></b-form-input>
                                                <div>
                                                    <div class='radio-btn'> 
                                                        <input type="radio" id="one" value="True" v-model="answer1">
                                                        <!-- <b-form-input v-model="question" placeholder="Enter question"></b-form-input> -->
                                                        <label for="one">True</label>
                                                        <br>
                                                        <input type="radio" id="two" value="False" v-model="answer1">
                                                        <label for="two">False</label>
                                                        <br>
                                                        <span>Answer: {{ answer1 }}</span>
                    

                                                    </div>
                                                </div>
                                            </div>
                                            
                                        </div>                                    
                                    </div>                                                                                                                            
                                </div>
                            </div>
                        </div>


                        <div class="row">
                        <div class="col-lg-8" id="TrainerViewCourseDetails" style="padding-bottom: 40px">
                            <div class="member-info" id="question">
                                <div class="float-container-mcq">
                                    <div class="float-child-left">
                                        <label for="question">Question 1: </label>
                                    </div>
                                    <div class="float-child-right">
                                        <b-form-input v-model="questionMCQ" placeholder="Enter question"></b-form-input>
                                        <div>
                                        <div class='radio-btn'>
                                            <!--<form action="">-->
                                                <fieldset>
                                                <div id="div1">
                                                    <input type="radio" name="radio-set" id="radio-1" :value="answerValue" v-model="answer2" />
                                                    <input type="text" class="tb" name="tb1" @input="answerValue=$event.target.value" placeholder="Option 1" />
                                                </div><br>
                                                <div id="div1">
                                                    <input type="radio" name="radio-set" id="radio-2" :value="answerValue" v-model="answer2" />
                                                    <input type="text" class="tb" name="tb2" @input="answerValue=$event.target.value" placeholder="Option 2" />
                                                </div><br>
                                                <div id="div1">
                                                    <input type="radio" name="radio-set" id="radio-3" :value="answerValue" v-model="answer2" />
                                                    <input type="text" class="tb" name="tb3" @input="answerValue=$event.target.value" placeholder="Option 3" />
                                                </div><br>
                                                <div id="div1">
                                                    <input type="radio" name="radio-set" id="radio-4" :value="answerValue" v-model="answer2" />
                                                    <input type="text" class="tb" name="tb4" @input="answerValue=$event.target.value" placeholder="Option 4" />
                                                </div>
                                                <div id="answer">
                                                    Answer: {{  answer2 }}
                                                </div><br>

                                                </fieldset>
                                           <!-- </form>-->
                                            <br>
                                        </div>
                                        </div>
                                    </div>    

                                    <!--<div id="app">
                                        <input type="radio" name="foodOptions" id="food_a" value="option1" v-model="food">
                                        <label for="food__a1">option1</label>
                                        <br>
                                        <input type="radio" name="foodOptions" id="food_b" :value="food">
                                        <label for="food_b">
                                                    <input type="number" @input="food = $event.target.value"> per day
                                        </label>
                                        <br>
                                        <input type="radio" name="foodOptions" id="food_c" value="option3" v-model="food">
                                        <label for="food_a3">option3</label>
                                        
                                        <div>
                                            {{ food }}
                                        </div>
                                    </div>-->

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
        questionTF: "",
        questionMCQ: "",
        answer1: "",
        answer2: "",
    }),
    methods: {
        testing: function(){
            if (this.questionTF != "" && this.questionMCQ != ""){
                console.log('yay')
                console.log(this.questionTF)
            }
            if (this.questionTF == "" || this.questionMCQ != "") {
                console.log('mcqIN')
            }
            if (this.questionTF != "" || this.questionMCQ == "") {
                console.log('TFin')
            }
            else {
                console.log('please enter a question')
            }
        },
    }
  };

</script>

