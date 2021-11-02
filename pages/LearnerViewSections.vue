<template>

  <div id="App">
    <LearnerHeader/>
    <main id="main">
      <div class="content">
      <section id="faq" class="faq section-bg">
        <div class="sidenav">
            <a href="#">Section 1</a>
            <a href="#" class="disabled">Section 2</a>
            <a href="#" class="disabled"> Section 3</a>
            <a href="#" class="disabled">Section 4</a>
        </div>
        
        <div class="container" data-aos="fade-up">
          <div class="section-title">
            <h2>{{courseName}}</h2>
            <h3> Section 1 Overview </h3>
            <p>
              {{ sectionOverview }} 
            </p>
          </div>

          <div class="faq-list">
            <ul>
              <li data-aos="fade-up" data-aos-delay="200">
                <!-- <i class="bx bx-help-circle icon-help"></i> -->
                <a
                  data-bs-toggle="collapse"
                  data-bs-target="#faq-list-2"
                  class="collapsed"
                  >Section 1: {{title}}
                  <i class="bx bx-chevron-down icon-show"></i
                  ><i class="bx bx-chevron-up icon-close"></i
                ></a>
                <div
                  id="faq-list-2"
                  class="collapse"
                  data-bs-parent=".faq-list"
                >
                <iframe :src="url" width="100%" height="500px"></iframe>
                
                <button type="button" @click="addClicks" class="btn btn-outline-success">Mark as Complete</button>
                </div>
              </li>

              <li data-aos="fade-up" data-aos-delay="300">
                <a
                  data-bs-toggle="collapse"
                  data-bs-target="#faq-list-3"
                  class="collapsed"
                  >Section 1: {{title}}
                  <i class="bx bx-chevron-down icon-show"></i
                  ><i class="bx bx-chevron-up icon-close"></i
                ></a>
                <div
                  id="faq-list-3"
                  class="collapse"
                  data-bs-parent=".faq-list"
                >
                  <div class="embed-responsive embed-responsive-16by9">
                      <iframe class="embed-responsive-item" src="https://spm-grp2-storage.s3.ap-southeast-1.amazonaws.com/XRX-101/Class2/Section1/TechSeries-Demo.mp4" sandbox allowfullscreen></iframe>
                  </div>
             
                  <button type="button" @click="addClicks" class="btn btn-outline-success">Mark as Complete</button>
                </div>
              </li>   
              
            </ul>
          </div>
            <div class="form-group" id="takequiz" v-if="clicks_array.length==numberOfSections">
                <button @click="takequiz" type="button" class="btn btn-primary" :disabled='isDisabled'>Take Quiz</button>
            </div>
        </div>
      </section>
    </div>
      
    </main>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: "App",
    data: () => ({
      courseName: 'Fundamentals of XXX',
      sectionOverview: 'Section 1 Overview Section 1 Overview Section 1 Overview Section 1 Overview Section 1 Overview Section 1 Overview ',
      title:'This is the title of the material',
      url: 'https://spm-grp2-storage.s3.ap-southeast-1.amazonaws.com/XRX-101/Class2/Section1/Project_Instructions.pdf',
      numberOfSections: 2,
      clicks_array: [],
      completed: false,
      disabled: false,
    }),

    methods: {
      addClicks () {
        this.clicks_array.push('check');
      },
    }
  }
</script>

