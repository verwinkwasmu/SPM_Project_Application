<template>
  <div id = "app">
      <TrainerHeader/>
       <section id="team" class="team section-bg">
         <div class="container" data-aos="fade-up">
            <button onclick="document.location='TrainerViewClasses'" type="button" class="btn btn-primary">Back to All classes</button>
             <div class="section-title">
                  <h2>View Class Learner's progress</h2>
                  <h3> Fundamentals of XXX </h3>
                  <h5> Class 1 </h5>
            </div>
            <div class="row">
                <table class="table">
                    <thead>
                        <tr>
                        <th scope="col">Learner ID</th>
                        <th scope="col">Learner Name</th>
                        <th scope="col">Progress</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <th scope="row">{{learner1.learnerID}}</th>
                        <td>{{learner1.learnerName}}</td>
                        <td><b-progress :max="max" show-progress animated><b-progress-bar :value="learner1.learnerProgress" :label="`${((learner1.learnerProgress / max) * 100).toFixed(2)}%`"></b-progress-bar></b-progress></td>
                        </tr>
                        <tr>
                        <th scope="row">{{learner2.learnerID}}</th>
                        <td>{{learner2.learnerName}}</td>
                        <td><b-progress :max="max" show-progress animated><b-progress-bar :value="learner2.learnerProgress" :label="`${((learner2.learnerProgress / max) * 100).toFixed(2)}%`"></b-progress-bar></b-progress></td>
                        </tr>
                        <tr>
                        <th scope="row">{{learner3.learnerID}}</th>
                        <td>{{learner3.learnerName}}</td>
                        <td><b-progress :max="max" show-progress animated><b-progress-bar :value="learner3.learnerProgress" :label="`${((learner3.learnerProgress / max) * 100).toFixed(2)}%`"></b-progress-bar></b-progress></td>
                        </tr>
                    </tbody>
                </table>
            </div>
         </div>
       </section>
  </div>
</template>

<script>
  export default {
    name: "App",

    // data() {
    //   return {
    //     value: 45,
    //     max: 100
    //   },
    // },
    // methods: {
    //   randomValue() {
    //     this.value = Math.random() * this.max
    //   }
    // }
    data: () => ({
    
    max: 100,

    learner1: 
      {
        learnerID: "001",
        learnerName: "Pukimak",
        learnerProgress: 60,
      },
    learner2: 
      {
        learnerID: "456",
        learnerName: "KPKB",
        learnerProgress: 20,
      },
    learner3: 
      {
        learnerID: "069",
        learnerName: "APA",
        learnerProgress: 96,
      },

  }),
  }
</script>
