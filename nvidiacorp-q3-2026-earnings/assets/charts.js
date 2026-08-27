/**
 * NVIDIA Q3 2026 ECharts Charts
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
  function baseLegend() {
    return { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
  }

  /* 1. chart-revenue-trend */
  (function () {
    var el = document.getElementById('chart-revenue-trend');
    if (!el) return;
    var cats = ['24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2','26Q3'];
    var revenue = [35.1, 39.3, 44.1, 46.7, 57.0, 68.1, 81.6, 96.2];
    var netIncome = [19.3, 22.1, 18.8, 26.4, 31.9, 43.0, 58.3, 59.7];
    render(el, {
      animation: false, color: [P.s1, P.s2], grid: makeGrid(),
      legend: baseLegend(),
      tooltip: { trigger: 'axis' },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: [
        { type: 'value', name: '营收(十亿美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
        { type: 'value', name: '净利润(十亿美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { show: false } }
      ],
      series: [
        { name: '营收', type: 'bar', yAxisIndex: 0, data: revenue, barMaxWidth: isMobile ? 18 : 30, itemStyle: { color: P.s1, borderRadius: [3,3,0,0] } },
        { name: '净利润', type: 'line', yAxisIndex: 1, data: netIncome, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: P.s2 }, itemStyle: { color: P.s2 } }
      ]
    });
  })();

  /* 2. chart-revenue-mix */
  (function () {
    var el = document.getElementById('chart-revenue-mix');
    if (!el) return;
    var data = [
      { name: '数据中心', value: 92.5 },
      { name: 'Graphics等非DC业务', value: 7.5 }
    ];
    var pieColors = [P.s1, P.s3, P.s4];
    var legendConf = isMobile
      ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: P.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    render(el, {
      animation: false, color: pieColors, legend: legendConf,
      tooltip: { trigger: 'item', formatter: '{b}: {c}%' },
      series: [{
        type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: P.surface, borderWidth: 2 },
        label: { show: !isMobile, color: P.text, fontSize: fs(12), formatter: '{d}%' },
        labelLine: { show: !isMobile },
        data: data
      }]
    });
  })();

  /* 3. chart-margin-trend */
  (function () {
    var el = document.getElementById('chart-margin-trend');
    if (!el) return;
    var cats = ['24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2','26Q3'];
    var gross = [74.6, 73.0, 60.5, 72.4, 73.4, 75.0, 74.9, 75.0];
    var net = [55.0, 56.2, 42.6, 56.5, 56.0, 63.1, 71.5, 62.0];
    render(el, {
      animation: false, color: [P.s1, P.s2], grid: makeGrid(), legend: baseLegend(),
      tooltip: { trigger: 'axis' },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '百分比(%)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: Object.assign({}, axisLabel(), { formatter: '{value}%' }), splitLine: { lineStyle: { color: P.grid } } },
      series: [
        { name: '毛利率', type: 'line', data: gross, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: P.s1 }, itemStyle: { color: P.s1 } },
        { name: '净利率', type: 'line', data: net, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: P.s2 }, itemStyle: { color: P.s2 } }
      ]
    });
  })();

  /* 4. chart-cashflow */
  (function () {
    var el = document.getElementById('chart-cashflow');
    if (!el) return;
    var cats = ['FY23','FY24','FY25','FY26'];
    var ocf = [56.4, 28.1, 64.1, 102.7];
    var capex = [1.8, 1.1, 3.2, 6.0];
    var fcf = [54.6, 27.0, 60.9, 96.7];
    render(el, {
      animation: false, color: [P.s1, P.s3, P.s2], grid: makeGrid(), legend: baseLegend(),
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: { type: 'category', data: cats, axisLabel: axisLabel(), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '十亿美元', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
      series: [
        { name: '经营现金流', type: 'bar', data: ocf, barMaxWidth: isMobile ? 14 : 26, itemStyle: { color: P.s1, borderRadius: [3,3,0,0] } },
        { name: '资本支出', type: 'bar', data: capex, barMaxWidth: isMobile ? 14 : 26, itemStyle: { color: P.s3, borderRadius: [3,3,0,0] } },
        { name: '自由现金流', type: 'bar', data: fcf, barMaxWidth: isMobile ? 14 : 26, itemStyle: { color: P.s2, borderRadius: [3,3,0,0] } }
      ]
    });
  })();

  /* 5. chart-kpi-trend */
  (function () {
    var el = document.getElementById('chart-kpi-trend');
    if (!el) return;
    var cats = ['24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2','26Q3'];
    var opIncome = [21.9, 24.0, 21.6, 28.4, 36.0, 44.3, 53.5, 63.7];
    var netMargin = [55.0, 56.2, 42.6, 56.5, 56.0, 63.1, 71.5, 62.0];
    render(el, {
      animation: false, color: [P.s1, P.s2], grid: makeGrid(), legend: baseLegend(),
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: [
        { type: 'value', name: '营业利润(十亿美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
        { type: 'value', name: '净利率(%)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: Object.assign({}, axisLabel(), { formatter: '{value}%' }), splitLine: { show: false } }
      ],
      series: [
        { name: '营业利润', type: 'bar', yAxisIndex: 0, data: opIncome, barMaxWidth: isMobile ? 16 : 26, itemStyle: { color: P.s1, borderRadius: [3,3,0,0] } },
        { name: '净利率', type: 'line', yAxisIndex: 1, data: netMargin, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: P.s2 }, itemStyle: { color: P.s2 } }
      ]
    });
  })();

  /* 6. chart-geo */
  (function () {
    var el = document.getElementById('chart-geo');
    if (!el) return;
    var data = [
      { name: '超大规模云厂商', value: 487 },
      { name: '非超大规模(ACI&E)', value: 400 },
      { name: 'Graphics及其他', value: 72 }
    ];
    var pieColors = [P.s1, P.s3, P.s5];
    var legendConf = isMobile
      ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: P.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    render(el, {
      animation: false, color: pieColors, legend: legendConf,
      tooltip: { trigger: 'item', formatter: '{b}: {c} 亿 ({d}%)' },
      series: [{
        type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: P.surface, borderWidth: 2 },
        label: { show: !isMobile, color: P.text, fontSize: fs(12), formatter: '{d}%' },
        labelLine: { show: !isMobile },
        data: data
      }]
    });
  })();

  /* 7. chart-radar */
  (function () {
    var el = document.getElementById('chart-radar');
    if (!el) return;
    var indicators = [
      { name: '营收规模', max: 100 },
      { name: '毛利率', max: 100 },
      { name: '净利率', max: 100 },
      { name: '营业利润率', max: 100 },
      { name: '数据中心占比', max: 100 }
    ];
    var cur = [100, 75.0, 62.0, 66.2, 92.5];
    var prev = [48.6, 72.4, 56.5, 60.8, 66.0];
    render(el, {
      animation: false, color: [P.s1, P.neutral], grid: { left: 20, right: 20, top: 30, bottom: 20 },
      legend: baseLegend(),
      tooltip: {},
      radar: { indicator: indicators, radius: '62%', splitArea: { areaStyle: { color: ['rgba(0,113,227,0.02)','rgba(0,113,227,0.04)'] } }, axisName: { color: P.textMuted, fontSize: fs(11) }, splitLine: { lineStyle: { color: P.grid } }, axisLine: { lineStyle: { color: P.grid } } },
      series: [{
        type: 'radar',
        data: [
          { name: '本期(26Q3)', value: cur, symbol: 'circle', symbolSize: 5, lineStyle: { width: 2, color: P.s1 }, itemStyle: { color: P.s1 }, areaStyle: { opacity: 0.15, color: P.s1 } },
          { name: '去年同期(25Q3)', value: prev, symbol: 'circle', symbolSize: 5, lineStyle: { width: 2, color: P.neutral }, itemStyle: { color: P.neutral }, areaStyle: { opacity: 0.1, color: P.neutral } }
        ]
      }]
    });
  })();
})();
