<template>
    <div id='app'>
        <LearnerHeader/>
        <section id="services" class="services section-bg">
        <div class="container" data-aos="fade-up">
              <div class="section-title">
                <h2>My Badges</h2>
              </div>
              <div class="row">
                  <div class="col" v-for="badge in badges" :key="badge.courseId">
                    <b-card
                      img-src="~/assets/img/badge.png"
                      img-alt="Image"
                      img-top
                      tag="article"
                      style="max-width: 15rem;"
                      class="mb-1"
                      :id="badge.courseId"
                    >
                      <b-card-text>
                        <h3>{{badge.courseName}} </h3>
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
import axios from 'axios';

 export default {
      name: "App",
      
  data: () => ({
      badges: [],
      learnerId: localStorage.getItem('userId')
  }),
  async created(){
    const apiUrl = `https://spm-flask.herokuapp.com/awardedBadges?learnerId=${this.learnerId}`
    try{
      let response = await axios.get(apiUrl);
      this.badges = response.data.data
    }catch(err){
      console.log(err)
    }
  }

};
</script>
