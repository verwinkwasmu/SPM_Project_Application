<template>
    <div>
        <Header/>
        <section id="team" class="team section-bg"> 
            <div class="container" data-aos="fade-up">
                <div class="row">
                    <div class="col-lg-8" id="createCourse" style="padding-bottom: 50px">
                    <div class="addEngineer">
                        <h5> Currently Enrolled: </h5>
                    </div>

                <b-tabs>
                    <b-tab-item label="Table">
                        <b-table
                        :data="data"
                            :columns="columns"
                            :checked-rows.sync="checkedRows"
                            :is-row-checkable="(row) "
                            checkable
                            :checkbox-position="checkboxPosition">
                        </b-table>
                    </b-tab-item>

                    <div class="Add">
                        <a href="EditClass" class="Add-btn">Add</a>
                    </div> <!-- Link to DB to refresh page with updated list-->     
                </b-tabs>
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
