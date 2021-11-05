<template>
    <div id='app'>
        <LearnerHeader/>
        <section id="services" class="services section-bg">
        <div class="container" data-aos="fade-up">
              <div class="section-title">
                <h2>My Badges</h2>
              </div>
              <div class="row">
                  <div class="col">
                    <b-card
                      img-src="~/assets/img/badge.png"
                      img-alt="Image"
                      img-top
                      tag="article"
                      style="max-width: 20rem;"
                      class="mb-1"
                      id="badge"
                    >
                      <b-card-text>
                        <h3> {{course1.courseName}} </h3>
                      </b-card-text>
                    </b-card>
                    
                  </div>
                  <div class="col">
                    <b-card
                      img-src="~/assets/img/badge.png"
                      img-alt="Image"
                      img-top
                      tag="article"
                      style="max-width: 20rem;"
                      class="mb-1"
                      
                    >
                      <b-card-text>
                        <h3> {{course2.courseName}} </h3>
                      </b-card-text>
                    </b-card>
                  </div>
                  <div class="col">
                    <b-card
                      img-src="~/assets/img/badge.png"
                      img-alt="Image"
                      img-top
                      tag="article"
                      style="max-width: 20rem;"
                      class="mb-1"
                    >
                      <b-card-text>
                        <h3> {{course2.courseName}} </h3>
                      </b-card-text>
                    </b-card>
                  </div>
                  <div class="col">
                    <b-card
                      img-src="~/assets/img/badge.png"
                      img-alt="Image"
                      img-top
                      tag="article"
                      style="max-width: 20rem;"
                      class="mb-1"
                    >
                      <b-card-text>
                        <h3> {{course2.courseName}} </h3>
                      </b-card-text>
                    </b-card>
                  </div>
                  <b-tooltip target="badge">Your badge is here!</b-tooltip>
              </div>
        </div>
        </section>
    </div>
</template>

<script>
 export default {
      name: "App",
      
  data: () => ({
    course1: 
      {
        badgeName: "Hi please answer the question",
        courseName: "SPM GOOOOO",
      },
      course2: 
      {
        badgeName: "Hi please answer the question",
        courseName: "SPM NOOOOO",
      },
  }),

};
</script>
