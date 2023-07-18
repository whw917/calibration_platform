<style scoped>

.main-page{
    width: 80%;
    margin: auto;
    
}
.name-bar{
    width: 300px;
    float:left;
}

.other-bar{
    width: 300px;
    float: left;
}

.point-bar{
    width: 90%;
    float: left;

    margin-top: 40px ;
}

.left-col{
    width:30%;
}

.right-col{
    offset: 1;
    width:30%;
}
.form-item-label {
    width: 30%; /* Adjust this value as needed */
}

.buttons{
    margin-top: 10px;
}



</style>

<template>
    <Form class="main-page">

        <Row> 
            <Col class="left-col">
                <FormItem class="form-item-label"  label="流程名称:" >
                    <Input class="name-bar" v-model="queryParam.flow_name" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="流程类型:">
                    <Select v-model="queryParam.flow_type" class="other-bar">
                        <Option v-for="item in flow_type_list" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>

                <FormItem class="form-item-label" label="驱动协议:">
                    <Select v-model="queryParam.driver" class="other-bar">
                        <Option v-for="item in driver_list" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>

                <FormItem class="form-item-label" label="传感器协议:">
                    <Select v-model="queryParam.sensor_protocol" class="other-bar">
                        <Option v-for="item in sensor_protocol_list" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>

                

            </Col>

            <Col  class="right-col"> 

                <FormItem class="form-item-label" label="设备名称:">
                    <Input class="other-bar" v-model="queryParam.device_name" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="设备协议:">
                    <Input class="other-bar" v-model="queryParam.device_protocol" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="运动时间(s):">
                    <Input class="other-bar" v-model="queryParam.move_seconds" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="读数延时(s):">
                    <Input class="other-bar" v-model="queryParam.wait_seconds" placeholder="name" clearable />
                </FormItem>
            </Col> 

            <Col class="right-col">
                <FormItem class="form-item-label" label="读数次数(次):">
                    <Input class="other-bar" v-model="queryParam.read_times" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="平台精度:">
                    <Input class="other-bar" v-model="queryParam.precise" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="传感器轴数:">
                    <Select v-model="queryParam.sensor_sum" class="other-bar">
                        <Option v-for="item in sensor_sum_list" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>

                <FormItem class="form-item-label" label="传感器名称:">
                    <Select v-model="queryParam.sensor_name" class="other-bar">
                        <Option v-for="item in sensor_name_list" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>
            
            </Col>

        </Row>
                <FormItem label="点数列表:"  class="point-bar">
                    <Input v-model="queryParam.scale_list" placeholder="name" size="large" clearable />

                    <Row class="buttons">
                    
                        <Col align="right">
                            <Button type="primary" @click="saveChanges" icon="search">确定</Button>
                            <Button type="primary" @click="cancelChanges">取消</Button>
                        </Col>
    
                    </Row>
                </FormItem>

                
                

         
    </Form>
</template>
  
  <script>
  import { Row, Input, Button, Table, Page, Space, FormItem, resolveComponent} from 'view-design'
  
  export default {
    components: {
    Input,
    Button,
    Table,
    Page,
    Space,
    FormItem,
    Row
},

    data() {
        return {
            //isPyWebViewReady: false,
            queryParam: {
                id: '',
                flow_name: '',
                flow_type: '',
                driver: '',
                sensor_protocol: '',
                device_name: '',
                device_protocol: '',
                move_seconds: '',
                wait_seconds: '',
                read_times: '',
                precise: '',
                sensor_sum: '',
                sensor_name: '',
                scale_list: '',
            },
            cityList: [
                    {
                        value: 'New York',
                        label: 'New York'
                    },
                    {
                        value: 'London',
                        label: 'London'
                    },
            ],
            flow_type_list: [
                {
                    value: '自动标定',
                    label: '自动标定'
                },
                {
                    value: '检验',
                    label: '检验'
                },
            ],
            driver_list: [
                {
                    value: '485',
                    label: '485'
                },
                {
                    value: 'AT',
                    label: 'AT'
                },
            ],
            sensor_protocol_list: [
                {
                    value: '485',
                    label: '485'
                },
                {
                    value: 'AT',
                    label: 'AT'
                },

            ],
            sensor_sum_list: [
                {
                    value: 1,
                    label: 1
                },
                {
                    value: 2,
                    label: 2
                },
                {
                    value: 3,
                    label: 3
                },

            ],
            sensor_name_list: [
                {
                    value: '单轴倾角',
                    label: '单轴倾角'
                },
                {
                    value: '双轴倾角',
                    label: '双轴倾角'
                },
                {
                    value: '三轴倾角',
                    label: '三轴倾角'
                },

            ],

        }
        },
        beforeCreate() {
            this.isPyWebViewReady = (typeof pywebview !== 'undefined');
        },

        created() {
            if (this.isPyWebViewReady) {
                this.fetchFlowData();
            }
        },

        mounted() {
            if (!this.isPyWebViewReady) {
                window.addEventListener('load', this.fetchFlowData);
            }
        },
        methods: {

            fetchFlowData() {
                console.log('ID:', this.$route.params.id);
                pywebview.api.getFlow(this.$route.params.id).then(response => {
                    if (response.code === 200) {
                        this.queryParam = response.result;
                    } else {
                        console.error('Error fetching flow data:', response.message);
                    }
                });
            },



            saveChanges() {
            console.log('ID:', this.$route.params.id);
                pywebview.api.editFlow(JSON.stringify(this.queryParam)).then(response => {
                    if (response.code === 200) {
                        console.log('Flow data updated successfully.');
                        this.$router.push({ name: 'FlowManagement' });  
                    } else {
                        console.error('Error updating flow data:', response.message);
                    }
                });
            },

            cancelChanges() {
                this.$router.push({ name: 'FlowManagement' });  
            }
        },
  }
  </script>