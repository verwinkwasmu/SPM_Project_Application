<template>
    <div>
        <TrainerHeader/>
        <section id="team" class="team section-bg">
            <div class="" data-aos="fade-up">
                <div class="section-title">
                  
                    <h2>Fundamentals of Xerox WorkCentre 7845 (Quiz)</h2>

                    <div class="row">
                        <div class="col-lg-8" id="TrainerViewCourseDetails" style="padding-bottom: 40px">
                            <!-- <div class="member d-flex align-items-start"
                                    data-aos="zoom-in"
                                    data-aos-delay="100"
                                   > -->
                                        
                                <div class="member-info" id="question">

                                    <div>
                                        <div class="float-container">
                                            <div class="float-child-left">
                                                <label for="question">Question 1: </label>
                                            </div>
                                            <div class="float-child-right">
                                                <b-form-input v-model="question" placeholder="Enter question"></b-form-input>
                                                <div>
                                                    <div class='radio-btn'> 
                                                        <input type="radio" id="one" value="True" v-model="answer">
                                                        <!-- <b-form-input v-model="question" placeholder="Enter question"></b-form-input> -->
                                                        <label for="one">True</label>
                                                        <br>
                                                        <input type="radio" id="two" value="False" v-model="answer">
                                                        <label for="two">False</label>
                                                        <br>
                                                        <span>Answer: {{ answer }}</span>
                    

                                                    </div>
                                                </div>
                                            </div>
                                            
                                        </div>
                                    
                                    </div>
                                    
                                        <!-- <div class="mt-2">Question is: {{ question }}</div> --> 

                                    <!-- <div>
                                        <div class="float-child-left"> 
                                            <input type="radio" id="one" value="True" v-model="answer">
                                            <label for="one">True</label>
                                            <br>
                                            <input type="radio" id="two" value="False" v-model="answer">
                                            <label for="two">False</label>

                                            <span>Answer: {{ answer }}</span>
                                        </div>
                                    </div> -->


                                    
                               
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
                                        <b-form-input v-model="question" placeholder="Enter question"></b-form-input>
                                        <div class='radio-btn'>
                                            <form action="">
                                                <fieldset>
                                                <div id="div1"><input class="rd" type="radio" name="radio-set" id="radio-1" value="Normal Radio" checked= /><input type="text" class="tb" name="tb1" value="" placeholder="Option 1" /></div><br>
                                                <div id="div1"><input class="rd" type="radio" name="radio-set" id="radio-1" value="Normal Radio" checked= /><input type="text" class="tb" name="tb1" value="" placeholder="Option 2" /></div><br>
                                                <div id="div1"><input class="rd" type="radio" name="radio-set" id="radio-1" value="Normal Radio" checked= /><input type="text" class="tb" name="tb1" value="" placeholder="Option 3" /></div><br>
                                                <div id="div1"><input class="rd" type="radio" name="radio-set" id="radio-1" value="Normal Radio" checked= /><input type="text" class="tb" name="tb1" value="" placeholder="Option 4" /></div>
                                                </fieldset>
                                            </form>
                                        </div>
                                    </div>
                                    <!-- <form action="">
                                        <fieldset>
                                                <div id="div1"><input class="rd" type="radio" name="radio-set" id="radio-1" value="Normal Radio" checked= /><input type="text" class="tb" name="tb1" value="" placeholder="Option 1" /></div><br>
                                                <div id="div1"><input class="rd" type="radio" name="radio-set" id="radio-1" value="Normal Radio" checked= /><input type="text" class="tb" name="tb1" value="" placeholder="Option 2" /></div><br>
                                                <div id="div1"><input class="rd" type="radio" name="radio-set" id="radio-1" value="Normal Radio" checked= /><input type="text" class="tb" name="tb1" value="" placeholder="Option 3" /></div><br>
                                                <div id="div1"><input class="rd" type="radio" name="radio-set" id="radio-1" value="Normal Radio" checked= /><input type="text" class="tb" name="tb1" value="" placeholder="Option 4" /></div>
                                        </fieldset>
                                    </form> -->
                                </div>
                            </div>
                        </div>
                    </div>   
                    </div>
                </div>
                <div class="buttongroup">
                    <div class="TrainerCreateQuiz">
                        <a href="TrainerCreateQuiz" class="TrainerCreateQuiz-btn">Create</a>
                    </div>

                    <div class="TrainerCancelQuiz">
                        <a href="TrainerCancelQuiz" class="TrainerCancelQuiz-btn">Cancel</a>
                    </div>
                </div>
                   
            <!-- </div> -->

        </section>
    </div>
</template>


<script>
  export default {
    data() {
      return {
        question: '',
        answer: ''
      }
    }
  }
</script>

