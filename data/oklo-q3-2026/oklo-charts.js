/**
 * Oklo Q3 2026 ECharts Charts
 */
(function () {
  'use strict';
  var rootStyle = getComputedStyle(document.documentElement);
  function cssVar(name, fallback) {
    var v = rootStyle.getPropertyValue(name);
    v = v ? v.trim() : '';
    return v || fallback;
  }
  var P = {
    primary:    cssVar('--accent',         '#0071e3'),
    accent:     cssVar('--accent',         '#0071e3'),
    positive:   cssVar('--accent2',        '#34c759'),
    negative:   cssVar('--neg',            '#d93025'),
    neutral:    cssVar('--muted',          '#6e6e73'),
    text:       cssVar('--ink',            '#1d1d1f'),
    textMuted:  cssVar('--muted',          '#6e6e73'),
    grid:       cssVar('--rule',           '#d2d2d7'),
    surface:    cssVar('--bg2',            '#ffffff'),
    s1: '#0071e3', s2: '#34c759', s3: '#ff9500', s4: '#af52de', s5: '#ff3b30'
  };
  var isMobile = window.innerWidth <= 700;
  function fs(b) { return isMobile ? Math.round(b * 0.86) : b; }
  function makeGrid() {
    return isMobile
      ? { left: 38, right: 16, top: 34, bottom: 58, containLabel: true }
      : { left: 56, right: 28, top: 42, bottom: 48, containLabel: true };
  }
  function axisLabel() { return { color: P.textMuted, fontSize: fs(12) }; }
  function makeChart(el) { return echarts.init(el, null, { renderer: 'svg' }); }
  function render(el, option) {
    if (!el) return null;
    var chart = makeChart(el);
    chart.setOption(option);
    window.addEventListener('resize', function () { chart.resize(); });
    return chart;
  }

  /* 1. chart-revenue-trend */
  (function () {
    var el = document.getElementById('chart-revenue-trend');
    if (!el) return;
    var cats = ['24Q3','24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var revenue = [0, 0, 0, 0, 0, 0, 0, 1.21];
    var netIncome = [-9.96, -10.29, -9.81, -24.69, -29.72, -41.45, -33.06, -48.54];
    var option = {
      animation: false, color: [P.s1, P.s2], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis' },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: [
        { type: 'value', name: '营收(百万美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
        { type: 'value', name: '净利润(百万美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { show: false } }
      ],
      series: [
        { name: '营收', type: 'bar', yAxisIndex: 0, data: revenue, barMaxWidth: isMobile ? 18 : 30, itemStyle: { color: P.s1, borderRadius: [3,3,0,0] } },
        { name: '净利润', type: 'line', yAxisIndex: 1, data: netIncome, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: P.s2 }, itemStyle: { color: P.s2 } }
      ]
    };
    render(el, option);
  })();

  /* 2. chart-revenue-mix */
  (function () {
    var el = document.getElementById('chart-revenue-mix');
    if (!el) return;
    var data = [
      { name: '同位素产品与服务', value: 70 },
      { name: '工程与开发服务', value: 51 }
    ];
    var colors = [P.s1, P.s3];
    var lg = isMobile ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: P.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false, color: colors, legend: lg,
      tooltip: { trigger: 'item', formatter: '{b}: ${c}万 ({d}%)' },
      series: [{ type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: P.surface, borderWidth: 2 },
        label: { show: !isMobile, color: P.text, fontSize: fs(12), formatter: '{d}%' }, labelLine: { show: !isMobile }, data: data }]
    };
    render(el, option);
  })();

  /* 3. chart-margin-trend */
  (function () {
    var el = document.getElementById('chart-margin-trend');
    if (!el) return;
    var cats = ['25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var gm = [-100, -100, -100, -100, -100, 40.4];
    var om = [-100, -100, -100, -100, -100, -605.0];
    var nm = [-100, -100, -100, -100, -100, -401.1];
    var option = {
      animation: false, color: [P.s1, P.s2, P.s3], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', formatter: function(p) { return p.map(function(x){ return x.marker + x.seriesName + ': ' + x.value + '%'; }).join('<br/>'); } },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '%', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
      series: [
        { name: '毛利率', type: 'line', data: gm, smooth: true, symbol: 'circle', symbolSize: fs(7), lineStyle: { width: 2.5 }, itemStyle: { color: P.s1 } },
        { name: '营业利润率', type: 'line', data: om, smooth: true, symbol: 'diamond', symbolSize: fs(7), lineStyle: { width: 2.5 }, itemStyle: { color: P.s2 } },
        { name: '净利率', type: 'line', data: nm, smooth: true, symbol: 'triangle', symbolSize: fs(8), lineStyle: { width: 2.5, type: 'dashed' }, itemStyle: { color: P.s3 } }
      ]
    };
    render(el, option);
  })();

  /* 4. chart-cashflow */
  (function () {
    var el = document.getElementById('chart-cashflow');
    if (!el) return;
    var cats = ['25Q3','25Q4','26Q1','26Q2'];
    var ocf = [-18.03, -33.43, -17.87, -47.59];
    var capex = [-5.05, -26.95, -32.81, -94.09];
    var fcf = [-23.08, -60.38, -50.68, -141.68];
    var option = {
      animation: false, color: [P.s2, P.s5, P.s1], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel()), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '百万美元', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
      series: [
        { name: '经营现金流', type: 'bar', data: ocf, barMaxWidth: isMobile ? 16 : 28, itemStyle: { color: P.s2, borderRadius: [3,3,0,0] } },
        { name: '资本支出', type: 'bar', data: capex, barMaxWidth: isMobile ? 16 : 28, itemStyle: { color: P.s5, borderRadius: [3,3,0,0] } },
        { name: '自由现金流', type: 'line', data: fcf, smooth: true, symbol: 'circle', symbolSize: fs(8), lineStyle: { width: 2.5, color: P.s1 }, itemStyle: { color: P.s1 } }
      ]
    };
    render(el, option);
  })();

  /* 5. chart-kpi-trend */
  (function () {
    var el = document.getElementById('chart-kpi-trend');
    if (!el) return;
    var cats = ['25Q3','25Q4','26Q1','26Q2'];
    var rd = [14.95, 24.59, 27.05, 39.47];
    var capex = [5.05, 26.95, 32.81, 94.09];
    var option = {
      animation: false, color: [P.s4, P.s3], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '百万美元', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
      series: [
        { name: '研发投入', type: 'bar', data: rd, barMaxWidth: isMobile ? 16 : 28, itemStyle: { color: P.s4, borderRadius: [3,3,0,0] } },
        { name: '资本支出', type: 'bar', data: capex, barMaxWidth: isMobile ? 16 : 28, itemStyle: { color: P.s3, borderRadius: [3,3,0,0] } }
      ]
    };
    render(el, option);
  })();

  /* 6. chart-geo */
  (function () {
    var el = document.getElementById('chart-geo');
    if (!el) return;
    var data = [{ name: '北美（美国）', value: 100 }];
    var colors = [P.s1];
    var lg = isMobile ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: P.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false, color: colors, legend: lg,
      tooltip: { trigger: 'item', formatter: '{b}: {d}%' },
      series: [{ type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: P.surface, borderWidth: 2 },
        label: { show: !isMobile, color: P.text, fontSize: fs(12), formatter: '{d}%' }, labelLine: { show: !isMobile }, data: data }]
    };
    render(el, option);
  })();

  /* 7. chart-radar */
  (function () {
    var el = document.getElementById('chart-radar');
    if (!el) return;
    var indicator = [
      { name: '营收规模', max: 10 }, { name: '现金储备', max: 100 },
      { name: '研发强度', max: 100 }, { name: '资本支出', max: 100 },
      { name: '盈利能力', max: 20 }, { name: '客户管线', max: 100 }
    ];
    var value = [1.2, 30, 100, 94, -49, 100];
    var option = {
      animation: false, color: [P.s1],
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: {},
      radar: {
        indicator: indicator, shape: 'polygon', splitNumber: 4,
        axisName: { color: P.textMuted, fontSize: fs(11) },
        splitArea: { areaStyle: { color: ['rgba(0,113,227,0.02)','rgba(0,113,227,0.04)','rgba(0,113,227,0.02)','rgba(0,113,227,0.04)'] } },
        splitLine: { lineStyle: { color: P.grid } }, axisLine: { lineStyle: { color: P.grid } }
      },
      series: [{ type: 'radar', data: [{ value: value, name: 'Q3 2026', areaStyle: { color: 'rgba(0,113,227,0.2)' }, lineStyle: { color: P.s1, width: 2 }, itemStyle: { color: P.s1 } }], symbol: 'circle', symbolSize: fs(6) }]
    };
    render(el, option);
  })();

})();
