$(document).ready(function () {
    var graph = new joint.dia.Graph();
    var paper = new joint.dia.Paper({
        el: $('#paper'),
        width: 1000,
        height: 1000,
        model: graph,
        gridSize: 10,
        drawGrid: true
    });

    function createAgent(x, y) {
        var agent = new joint.shapes.standard.Rectangle();
        agent.resize(100, 40);
        agent.position(x, y);
        agent.attr({
            body: { fill: '#2ECC71', stroke: '#000', strokeWidth: 1 },
            label: { text: 'Agent', fill: '#000' }
        });
        return agent;
    }

    function createHost(x, y) {
        var host = new joint.shapes.standard.Circle();
        host.resize(80, 80);
        host.position(x, y);
        host.attr({
            body: { fill: '#0074D9', stroke: '#000', strokeWidth: 1 },
            label: { text: 'Host', fill: '#000', refY: 40 }
        });
        return host;
    }

    $('#addAgent').on('click', function () {
        var agent = createAgent(10, 10);
        graph.addCell(agent);
    });

    $('#addHost').on('click', function () {
        var host = createHost(150, 10);
        graph.addCell(host);
    });

    $('#exportLayout').on('click', function () {
        var layout = {
            agents: [],
            hosts: []
        };

        graph.getElements().forEach(function (element) {
            var position = element.position();
            var type = element.attr('label/text');
            var item = { x: position.x, y: position.y };

            if (type === 'Agent') {
                layout.agents.push(item);
            } else if (type === 'Host') {
                layout.hosts.push(item);
            }
        });

        var layoutJSON = JSON.stringify(layout, null, 2);
        console.log(layoutJSON);
        // Export the layoutJSON to a file or send it to the server for further processing.
    });
});
