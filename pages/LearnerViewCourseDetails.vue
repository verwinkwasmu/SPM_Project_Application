<template>
    <div>
        <Header/>



        <section id="team" class="team section-bg">  <!--box-->
            <div class="container" data-aos="fade-up">

                <div class="section-title">
                    <h2>Fundamentals of Xerox WorkCentre 7845 <br></h2>
                </div>
                    <div class="row">
                        <div class="col-lg-8" id="createCourse" style="padding-bottom: 50px">
                            <div
                                class="member d-flex align-items-start"
                                data-aos="zoom-in"
                                data-aos-delay="100"
                            >
                                <div class="LearnerEnrol">
                                     <a href="LearnerViewClass" @click="enrol" class="LearnerEnrol-btn" v-if="notEnrolled">Enrol into course</a>
                                </div>

                                <span class="badge badge-success" v-if="enrolled">Already Enrolled</span>
                                
                                <div class="member-info">
                                <h4>Fundamentals of Xerox WorkCentre 7845</h4>
                                Prerequisite Courses: 
                                <ul>
                                    <li>Fundamentals of Xerox</li>
                                    <li>Fundamentals of Printing</li>
                                </ul>
                                
                                <h4>Course Description: </h4>
                                <p>
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
                                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                                </p>
                                </div>
                            </div>

                            <div class="LearnerWithdraw">  
                                <a href="" class="LearnerWithdraw-btn" v-if="enrolled">Withdraw from Course</a>
                            </div>  <!--if true, this button will show, if false, this button will not show. -->
                            
                        </div>     
                    </div>
            </div>

        </section>
    </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
      notEnrolled: true,
      enrolled: false,
  }),

  methods: {
      enrol () {

      }
  }
};
</script>
