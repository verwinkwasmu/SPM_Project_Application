<template>
    <div>
        <Header/>

        <!--<Homepage/>
       -->
        <section id="team" class="team section-bg">  <!--box-->
            <div class="container" data-aos="fade-up">

                <div class="section-title">
                    <h2>Fundamentals of Xerox WorkCentre 7845 <br> <br> Class 1</h2>
                </div>
                    <div class="row">
                        <div class="col-lg-8" id="createCourse" style="padding-bottom: 50px">
                            <div
                                class="member d-flex align-items-start"
                                data-aos="zoom-in"
                                data-aos-delay="100"
                            >
                                
                                <div class="member-info">
                                <h4>Fundamentals of Xerox WorkCentre 7845</h4>
                                Prerequisite Courses: 
                                <ul>
                                    <li>Fundamentals of Xerox</li>
                                    <li>Fundamentals of Printing</li>
                                </ul>
                                
                                <h4>Maximum Class Size: </h4> <p>30</p> <br>
                                <h4>Period of Enrollment: </h4> <p>1st July - 30th July</p> <br>
                                <h4>Course Description: </h4>
                                <p>
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
                                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                                </p>
                                </div>
                            </div>
                        </div>
                
                        <div class="col-lg-8 mt-4 mt-lg-0" id="createCourse" > 

                            <div class="member-info" style="padding-bottom: 100px">
                                    <h5>Assign a Trainer: </h5> 
                                        <b-select>
                                            <optgroup label="Sales Department">
                                                <option value="left">Halim</option>
                                                <option value="right">Mark</option>
                                            </optgroup>
                                                <optgroup label="Leasing Department">
                                                <option value="Bob">Bob</option>
                                                <option value="Ali">Ali</option>
                                                </optgroup>
                                        </b-select>
                                    
                            </div>


                            
                            <div class="addEngineer">
                                <h5> Currently Enrolled: </h5>
                                <a href="AddEngineer" class="addEngineer-btn">Add New Engineers</a>
                            </div>

                            <!--<section id="team" class="team section-bg">-->
                                <b-tabs>
                                    <b-tab-item label="Table">
                                        <b-table
                                            :data="data"
                                            :columns="columns"
                                            :checked-rows.sync="checkedRows"
                                            :is-row-checkable="(row) "
                                            checkable
                                            :checkbox-position="checkboxPosition">

                                            <!-- <template #bottom-left>
                                                <b>Total checked</b>: {{ checkedRows.length }}
                                            </template> -->
                                        </b-table>
                                    </b-tab-item>

                                <div class="remove">
                                    <a href="EditClass" class="remove-btn">Remove</a>
                                </div> <!-- Link to DB to refresh page with updated list-->

                                    <!-- <b-tab-item label="Checked rows">
                                        <pre>{{ checkedRows }}</pre>
                                    </b-tab-item> -->
                                </b-tabs>
                                <!-- </div> -->
                            <!--</section>-->
                        </div>

                    </div>
            </div>

        </section>
    </div>
</template>

<script>
        export default {
            data() {
                const data = [
                    { 'id': 1, 'engineer_name': 'Jesse Simmons'},
                    { 'id': 2, 'engineer_name': 'John Jacobs'},
                    { 'id': 3, 'engineer_name': 'Tina Gilbert'},
                    { 'id': 4, 'engineer_name': 'Clarence Flores'},
                    { 'id': 5, 'engineer_name': 'Anne Lee'}
                ]

                return {
                    data,
                    checkboxPosition: 'right',
                    checkedRows: [],
                    columns: [
                        {
                            field: 'id',
                            label: 'ID',
                            width: '40',
                            numeric: true
                        },
                        {
                            field: 'engineer_name',
                            label: 'Engineer Name',
                        }
                    ]
                }
            }
        }
</script>  
