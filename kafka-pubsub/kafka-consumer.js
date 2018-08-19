var Kafka = require('no-kafka');
var consumer = new Kafka.SimpleConsumer();

// data handler function can return a Promise
var dataHandler = function (messageSet, topic, partition) {
    messageSet.forEach(function (m) {
        console.log(topic, partition, m.offset, m.message.value.toString('utf8'));
    });
};

consumer.init().then(function () {
    // Subscribe partitons 0 in a topic:
    return consumer.subscribe('Area1-Zone1', [0], dataHandler);
});

