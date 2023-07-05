<style>
.rate-demo {
    display: flex;
    justify-content: space-between;
    align-items: center;   
}
</style>
<template>
    <Modal
        v-model="modal"
        title="串口配置"
        @on-ok="ok"
        @on-cancel="cancel">
        <Card style="width:100%">
            <template #title>
                <p>编码器</p>
            </template>
            <template #extra>               
                
            </template>
            <Row>
                <i-col span="12"> <p>串口</p></i-col>
                <i-col span="12">
                    <div class="div-select-com">
                        <Select v-model="comAngulayEncoder">
                            <Option v-for="item in serialList" :value="item.name" :key="item.name">{{ item.title }}</Option>
                        </Select>
                    </div>
                </i-col>
            </Row>
            
        </Card>
        <Card style="width:100%">
            <template #title>
                <p>步进电机</p>
            </template>
            <template #extra>               
                
            </template>
            <Row>
                <i-col span="12"> <p>串口</p></i-col>
                <i-col span="12">
                    <div class="div-select-com">
                        <Select v-model="comStepMotor">
                            <Option v-for="item in serialList" :value="item.name" :key="item.name">{{ item.title }}</Option>
                        </Select>
                    </div>
                </i-col>
            </Row>
        </Card>
    </Modal>
</template>
<script>

function setOptions(section, option_name, option_value, callback) {
  pywebview.api.setOptions(section, option_name, option_value).then(res => {
    // alert(res)
    // let jsonRsult = JSON.parse(res)
    callback(res)
  })
}

    export default {
        name: 'SerialConifg',
        props: {
            visible: {
                type: Boolean,
                default: false,
            },
            modalShow:{
                type: Boolean,
                default: false,
            },
            id:{  
                type: String,
                default: "",
            },
        },
        watch:{
            'visible':function(val, oldVal){
                if(val!=oldVal){
                     this.modal =val
                }
            },
            
            'modalShow':function(val, oldVal){
                if(val!=oldVal){
                     this.modal =val
                }
            },
        },
        data () {
            return {
                modal: true,
                serialList: [
                    {
                    name: 'COM10',
                    title: 'COM10'
                    },
                    {
                    name: 'COM11',
                    title: 'COM11'
                    }

                ],
                comAngulayEncoder: "",
                comStepMotor: "",
              
            }
        },
        created(){
            console.log("serial config")
        },
        mounted () {
        },
        methods: {
            init(lstSerial){
                this.serialList = lstSerial
            },
            ok () {
                setOptions("ANGULAR_ENCODER", "port", this.comAngulayEncoder, res=>{
                    if(res.code == 200 ){
                        this.$Message.info('修改编码器串口成功');
                    }
                    else{
                        this.$Message.info('修改编码器串口失败');
                    }
                })
                setOptions("STEP_MOTOR", "port", this.comStepMotor, res=>{
                    if(res.code == 200 ){
                        this.$Message.info('修改编步进电机串口成功');
                    }
                    else{
                        this.$Message.info('修改步进电机串口失败');
                    }
                })
                this.$emit("onClickOk")
            },
            cancel () {
                this.$emit("onClickCancel")
            }
        },
    }
</script>
