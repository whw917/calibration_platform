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
        title="协议配置"
        @on-ok="ok"
        @on-cancel="cancel">
        <div class="div-work-mode">
            <RadioGroup v-model="protocolName" vertical>
              <Radio label="AT">
                <Icon></Icon>
                <span>AT协议</span>
              </Radio>
              <Radio label="MODBUS">
                <Icon></Icon>
                <span>MODBUS协议</span>

              </Radio>
            </RadioGroup>
          </div>
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
        name: 'ProtocolConifg',
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
                protocolName: "",              
            }
        },
        created(){
            
        },
        mounted () {
        },
        methods: {
            ok () {
                setOptions("SENSOR_PARAMS", "protocol", this.protocolName, res=>{
                    if(res.code == 200 ){
                        this.$Message.info('修改编码器串口成功');
                    }
                    else{
                        this.$Message.info('修改编码器串口失败');
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
