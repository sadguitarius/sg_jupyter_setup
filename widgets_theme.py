from IPython.core.display import HTML, display


def set_css_in_cell_output():
    display(HTML('''
    <style>
    :root {
      --dracula-dark-background: #21222c;
      --dracula-background: #282a36;
      --dracula-selection: #44475a;
      --dracula-foreground: #f8f8f2;
      --dracula-comment: #6272a4;
      --dracula-cyan: #8be9fd;
      --dracula-green: #50fa7b;
      --dracula-orange: #ffb86c;
      --dracula-pink: #ff79c6;
      --dracula-purple: #bd93f9;
      --dracula-red: #ff5555;
      --dracula-yellow: #f1fa8c;

      --jp-ui-font-color0: rgba(248, 248, 242, 1);
      --jp-ui-font-color1: rgba(248, 248, 242, 0.87);
      --jp-ui-font-color2: rgba(248, 248, 242, 0.54);
      --jp-ui-font-color3: rgba(248, 248, 242, 0.38);

      --jp-border-color1: #313341;

      --jp-layout-color1: #21222c;
      --jp-layout-color2: #253340;
      --jp-layout-color3: #44475a;

      --jp-brand-color0: #282a36;
      --jp-brand-color1: #bd93f9;

      --jp-warn-color0: var(--md-orange-700);
      --jp-warn-color1: var(--md-orange-500);

      --jp-error-color0: var(--md-red-700);
      --jp-error-color1: var(--md-red-500);

      --jp-success-color0: var(--md-green-700);
      --jp-success-color1: var(--md-green-500);

      --jp-info-color0: var(--md-cyan-700);
      --jp-info-color1: var(--md-cyan-500);

      --jp-widgets-color: var(--jp-ui-font-color0);
      --jp-widgets-label-color: var(--jp-widgets-color);
      --jp-widgets-readout-color: var(--jp-widgets-color);
      --jp-widgets-slider-handle-border-color: var(--jp-border-color1);
      --jp-widgets-slider-handle-background-color: var(--dracula-foreground);
      --jp-widgets-slider-active-handle-color: var(--jp-brand-color1);
      --jp-widgets-input-color: var(--jp-ui-font-color1);
      --jp-widgets-input-background-color: var(--jp-layout-color1);
      --jp-widgets-input-border-color: var(--jp-border-color1);
      --jp-widgets-input-focus-border-color: var(--jp-brand-color1);
    }

    .jupyter-widgets {
        color: var(--jp-widgets-color);
    }
    .jupyter-button {
        color: var(--jp-ui-font-color1);
        background-color: var(--jp-layout-color2);
        border-color: var(--jp-border-color1);
    }

    .jupyter-button:active, .jupyter-button.mod-active {
        color: var(--jp-ui-font-color1);
        background-color: var(--jp-layout-color3);
    }

    .jupyter-button:focus:enabled {
        outline: 1px solid var(--jp-widgets-input-focus-border-color);
    }

    .jupyter-button.mod-primary {
        color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
        background-color: var(--jp-brand-color1);
    }

    .jupyter-button.mod-primary.mod-active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-brand-color0);
    }

    .jupyter-button.mod-primary:active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-brand-color0);
    }

    /* Button "Success" Styling */

    .jupyter-button.mod-success {
        color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
        background-color: var(--jp-success-color1);
    }

    .jupyter-button.mod-success.mod-active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-success-color0);
    }

    .jupyter-button.mod-success:active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-success-color0);
    }

     /* Button "Info" Styling */

    .jupyter-button.mod-info {
        color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
        background-color: var(--jp-info-color1);
    }

    .jupyter-button.mod-info.mod-active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-info-color0);
    }

    .jupyter-button.mod-info:active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-info-color0);
    }

    /* Button "Warning" Styling */

    .jupyter-button.mod-warning {
        color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
        background-color: var(--jp-warn-color1);
    }

    .jupyter-button.mod-warning.mod-active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-warn-color0);
    }

    .jupyter-button.mod-warning:active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-warn-color0);
    }

    /* Button "Danger" Styling */

    .jupyter-button.mod-danger {
        color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
        background-color: var(--jp-error-color1);
    }

    .jupyter-button.mod-danger.mod-active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-error-color0);
    }

    .jupyter-button.mod-danger:active {
        color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
        background-color: var(--jp-error-color0);
    }

    .widget-label-basic {
        color: var(--jp-widgets-label-color);
    }

    .widget-label {
        color: var(--jp-widgets-label-color);
    }

    .widget-inline-hbox .widget-label {
        color: var(--jp-widgets-label-color);
    }

    .widget-inline-vbox .widget-label {
        color: var(--jp-widgets-label-color);
    }

    .widget-readout {
        color: var(--jp-widgets-readout-color);
    }

    .widget-valid.mod-valid i:before {
        color: green;
    }

    .widget-valid.mod-invalid i:before {
        color: red;
    }

    .widget-text input[type="text"], .widget-text input[type="number"], .widget-text input[type="password"], .widget-textarea textarea {
        border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
        background-color: var(--jp-widgets-input-background-color);
        color: var(--jp-widgets-input-color);
    }

    .widget-text input:focus, .widget-textarea textarea:focus {
        border-color: var(--jp-widgets-input-focus-border-color);
    }

    .widget-slider .ui-slider {
        /* Slider Track */
        border: var(--jp-widgets-slider-border-width) solid var(--jp-layout-color3);
        background: var(--jp-layout-color3);
    }

    .widget-slider .ui-slider .ui-slider-handle {
        /* Slider Handle */
        background-color: var(--jp-widgets-slider-handle-background-color);
        border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-handle-border-color);
    }

    /* Override jquery-ui */
    .widget-slider .ui-slider .ui-slider-handle:hover, .widget-slider .ui-slider .ui-slider-handle:focus {
        background-color: var(--jp-widgets-slider-active-handle-color);
        border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-active-handle-color);
    }

    .widget-slider .ui-slider .ui-slider-handle:active {
        background-color: var(--jp-widgets-slider-active-handle-color);
        border-color: var(--jp-widgets-slider-active-handle-color);
    }

    .widget-slider  .ui-slider .ui-slider-range {
        /* Interval between the two specified value of a double slider */
        background: var(--jp-widgets-slider-active-handle-color);
    }

    .progress-bar {
        background-color: var(--jp-brand-color1);
    }

    .progress-bar-success {
        background-color: var(--jp-success-color1);
    }

    .progress-bar-info {
        background-color: var(--jp-info-color1);
    }

    .progress-bar-warning {
        background-color: var(--jp-warn-color1);
    }

    .progress-bar-danger {
        background-color: var(--jp-error-color1);
    }

    .progress {
        background-color: var(--jp-layout-color2);
        border: none;
        box-shadow: none;
    }


    .widget-dropdown > select {
        border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
        background-color: var(--jp-widgets-input-background-color);
        color: var(--jp-widgets-input-color);
    }

    .widget-dropdown > select:focus {
        border-color: var(--jp-widgets-input-focus-border-color);
    }

    .widget-select > select {
        border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
        background-color: var(--jp-widgets-input-background-color);
        color: var(--jp-widgets-input-color);
    }

    .widget-select > select:focus {
        border-color: var(--jp-widgets-input-focus-border-color);
    }

    .widget-colorpicker input[type="color"] {
        background: var(--jp-widgets-input-background-color);
        color: var(--jp-widgets-input-color);
        border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    }

    .widget-colorpicker.concise input[type="color"] {
        border-left: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    }

    .widget-colorpicker input[type="color"]:focus, .widget-colorpicker input[type="text"]:focus {
        border-color: var(--jp-widgets-input-focus-border-color);
    }

    .widget-colorpicker input[type="text"] {
        background: var(--jp-widgets-input-background-color);
        color: var(--jp-widgets-input-color);
        border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    }

    .widget-datepicker input[type="date"] {
        border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
        background-color: var(--jp-widgets-input-background-color);
        color: var(--jp-widgets-input-color);
    }

    .widget-datepicker input[type="date"]:focus {
        border-color: var(--jp-widgets-input-focus-border-color);
    }

    .widget-datepicker input[type="date"]:invalid {
        border-color: var(--jp-warn-color1);
    }

    .jupyter-widgets.widget-tab > .widget-tab-contents {
        background: var(--jp-layout-color1);
        color: var(--jp-ui-font-color1);
        border: var(--jp-border-width) solid var(--jp-border-color1);
    }

    .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
        background: var(--jp-layout-color2);
        color: var(--jp-ui-font-color2);
        border: var(--jp-border-width) solid var(--jp-border-color1);
    }

    .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current {
        color: var(--jp-ui-font-color0);
        background: var(--jp-layout-color1);
    }

    .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current:before {
        background: var(--jp-brand-color1);
    }

    .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:hover:not(.p-mod-current) {
        background: var(--jp-layout-color1);
        color: var(--jp-ui-font-color1);
    }

    .p-Collapse-header {
        color: var(--jp-ui-font-color2);
        background-color: var(--jp-layout-color2);
        border: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    }

    .p-Collapse-header:hover {
        background-color: var(--jp-layout-color1);
        color: var(--jp-ui-font-color1);
    }

    .p-Collapse-open > .p-Collapse-header {
        background-color: var(--jp-layout-color1);
        color: var(--jp-ui-font-color0);
    }

    .p-Collapse-contents {
        background-color: var(--jp-layout-color1);
        color: var(--jp-ui-font-color1);
        border-left: var(--jp-widgets-border-width) solid var(--jp-border-color1);
        border-right: var(--jp-widgets-border-width) solid var(--jp-border-color1);
        border-bottom: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    }

    .cell-output-ipywidget-background {
    background-color: transparent !important;
    }
    </style>'''))


get_ipython().events.register('pre_run_cell', set_css_in_cell_output)
